from flask import Flask, jsonify, request
from flask_cors import CORS
import get_functions
from insert_data import insert_functions
import login_check

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"]) # we add our website here after code completion


def register_get_route(route, get_function, error_message):
    @app.route(route)
    def handler(id):
        result = get_function(id)
        if result:
            return jsonify(result)
        else:
            return jsonify({"error": error_message}), 404

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


### API calls for the additions

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

if __name__ == '__main__':
    app.run(debug=True)