from flask import Flask, jsonify, request
from flask_cors import CORS
from .insert_data import add_data
from . import get_functions
from . import login_check
from backend.src.insert_data.insert_functions import insert_volunteers
from .assignment_functions.assignment_routes import assignment_bp
from .edit_profile_functions.edit_profile_routes import edit_profile_bp
from .subcoord_functions.subcoord_routes import subcoord_bp
from .edit_class_functions.edit_class_routes import edit_class_info_bp
from .get_function_specifications.get_specifications_routes import get_specifications_bp
from .sub_to_volunteer.sub_to_volunteer_route import sub_to_list_bp
from .delete.delete_route import delete_bp
from .cancel_application.cancel_application_routes import cancel_application_bp


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"]) # we add our website here after code completion

# Helper functions
def register_get_route(route, get_function, error_message):
    def handler(id):
        data = get_function(id)
        return jsonify(data) if data else (jsonify({"error": error_message}), 404)

    endpoint = f"get_{get_function.__name__}"
    app.add_url_rule(route, endpoint=endpoint, view_func=handler)


def register_insert_route(route, insert_function, required_fields=None):
    def handler():
        data = request.get_json() or {}
        if required_fields:
            missing = [f for f in required_fields if f not in data]
            if missing:
                return jsonify({"error": f"Missing required fields: {', '.join(missing)}"}), 400

        ok = insert_function(**data)
        return (jsonify({"message": "Insertion successful"}), 201) if ok \
             else (jsonify({"error": "Insertion failed"}), 500)

    endpoint = f"insert_{insert_function.__name__}"
    app.add_url_rule(route, endpoint=endpoint, view_func=handler, methods=["POST"])



### API calls for the info
register_get_route("/api/teacher/<string:id>", get_functions.get_teacher_info, "Teacher not found")
register_get_route("/api/substitute/<string:id>", get_functions.get_substitute_info, "Substitute not found")
register_get_route("/api/feedback_to_sub/<string:id>", get_functions.get_feedback_to_sub, "Feedback not found")
register_get_route("/api/feedback_to_teacher/<string:id>", get_functions.get_feedback_to_teacher, "Feedback not found")
register_get_route("/api/availability/<string:id>", get_functions.get_availability, "Availability not found")
register_get_route("/api/preference/<string:id>", get_functions.get_single_substitute_preference, "Preference not found")
register_get_route("/api/class/<string:id>", get_functions.get_class_info, "Class not found")
register_get_route("/api/school/<string:id>", get_functions.get_school_info, "School not found")
register_get_route("/api/assignment/<string:id>", get_functions.get_single_assignment, "Assignment not found")


### API calls for inserting data
register_insert_route("/api/teacher", add_data.add_teacher, required_fields=["name", "phone_number", "school_name", "email", "password"])
register_insert_route("/api/substitute", add_data.add_substitute, required_fields=["name", "phone_number", "email", "password", "experience"])
register_insert_route("/api/feedback_to_sub", add_data.add_feedback_to_sub, required_fields=["date", "rating", "comments", "teacher_ID", "substitute_ID"])
register_insert_route("/api/feedback_to_teacher", add_data.add_feedback_to_teacher, required_fields=["date", "comments", "teacher_ID", "substitute_ID"])
register_insert_route("/api/availability", add_data.add_availability, required_fields=["substitute_ID", "beginning_date", "ending_date", "location"])
register_insert_route("/api/preference", add_data.add_substitute_preference, required_fields=["grade", "substitute_ID", "school_name", "subject", "location"])
register_insert_route("/api/class", add_data.add_class, required_fields=["subject", "grade", "beginning_time", "ending_time", "teacher_ID", "room", "school_ID"])
register_insert_route("/api/school", add_data.add_school, required_fields=["school_name"])
register_insert_route("/api/assignment", add_data.add_assignment, required_fields=["date", "notes", "status", "class_ID", "teacher_ID", "substitute_ID"])

register_insert_route("/api/volunteers", insert_volunteers, required_fields=["substitute_ID", "class_ID"])


app.register_blueprint(assignment_bp)
app.register_blueprint(edit_profile_bp)
app.register_blueprint(subcoord_bp)
app.register_blueprint(edit_class_info_bp)
app.register_blueprint(get_specifications_bp)
app.register_blueprint(sub_to_list_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(cancel_application_bp)

@app.route("/api/login", methods=['POST'])
def password_check():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user_data = login_check.check_password(email, password)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route("/")
def index():
    """Simple sanity-check so / shows something useful."""
    return jsonify({"status": "API is running 🚀"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)