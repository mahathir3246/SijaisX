from flask import Blueprint, request, jsonify
from .edit_class_queries import edit_class_info

edit_class_info_bp = Blueprint("edit_class_info_bp", __name__)

@edit_class_info_bp.route("/api/edit_class/<string:class_ID>", methods=["PATCH"])
def edit_class_info_route(class_ID):
    data = request.json
    teacher_ID = data.get("teacher_ID")
    subject = data.get("subject")
    grade = data.get("grade")
    beginning_time = data.get("beginning_time")
    ending_time = data.get("ending_time")
    duration = data.get("duration")
    room = data.get("room")

    result = edit_class_info(class_ID, teacher_ID, subject, grade,
                             beginning_time, ending_time, duration, room)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

