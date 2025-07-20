from flask import Blueprint, request, jsonify
from .get_specifications_routes import (get_teacher_classes_within_range)

get_specifications_bp = Blueprint("get_specifications_bp", __name__)

@get_specifications_bp.route("/api/get_specifications/teacher_classes/<string:teacher_ID>", methods=["GET"])
def api_get_teacher_classes_within_range(teacher_ID):
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if not start_date or not end_date:
        return jsonify({"success": False, "error": "Start date and end date are required"})
    
    result = get_teacher_classes_within_range(teacher_ID, start_date, end_date)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200
