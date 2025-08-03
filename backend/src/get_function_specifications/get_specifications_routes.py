from flask import Blueprint, request, jsonify
from .get_specifications_queries import (get_teacher_classes_within_range, get_all_assignment_of_teacher,
                                         get_all_assignments_of_school, get_all_assignments_available_to_sub,
                                         get_all_schools_of_sub)

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

@get_specifications_bp.route("/api/get_specifications/all_assignments_teacher/<string:teacher_ID>", methods=["GET"])
def api_get_all_assignments_of_teacher(teacher_ID):
    result = get_all_assignment_of_teacher(teacher_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/all_assignments_school/<string:school_ID>", methods=["GET"])
def api_get_all_assignments_of_school(school_ID):
    result = get_all_assignments_of_school(school_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/all_assignments_to_substitute/<string:substitute_ID>", methods=["GET"])
def api_get_all_assignments_to_substitute(substitute_ID):
    result = get_all_assignments_available_to_sub(substitute_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/all_schools_of_substitute/<string:substitute_ID>", methods=["GET"])
def api_get_all_schools_of_substitute(substitute_ID):
    result = get_all_schools_of_sub(substitute_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200
