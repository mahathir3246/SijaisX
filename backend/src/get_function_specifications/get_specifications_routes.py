from flask import Blueprint, request, jsonify
from .get_specifications_queries import *
from datetime import datetime


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

@get_specifications_bp.route("/api/get_specifications/get_accepted_batch_for_substitute/<string:substitute_ID>", methods=["GET"])
def api_get_accepted_batch_for_substitute(substitute_ID):
    result = get_assignments_accepted_by_sub_as_batch(substitute_ID)
    if not result["success"]:
        if "No assignments found" in result["error"]:
            return jsonify({"success": True, "batches": []}), 200
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/get_available_batch_for_substitute/<string:substitute_ID>", methods=["GET"])
def api_get_available_batch_for_substitute(substitute_ID):
    result = get_available_assignments_of_sub_as_batch(substitute_ID)
    if not result["success"]:
        if "No assignments found" in result["error"]:
            return jsonify({"success": True, "batches": []}), 200
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/get_batch_volunteers/<string:batch_ID>", methods=["GET"])
def api_get_batch_volunteers(batch_ID):
    requester_ID = request.args.get("requester_ID")  
    if not requester_ID:
        return jsonify({"success": False, "error": "Not logged in"}), 401
    result = get_batch_volunteers(batch_ID, requester_ID)
    if not result["success"]:
        status = 403 if result["error"] == "Access denied" else 400
        return jsonify(result), status
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/get_applied_batches_of_substitute/<string:substitute_ID>", methods=["GET"])
def api_get_applied_batches_of_substitute(substitute_ID):
    result = get_all_applied_batches_of_sub(substitute_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@get_specifications_bp.route("/api/get_specifications/get_completed_batches/<string:teacher_ID>", methods=["GET"])
def api_get_completed_batches(teacher_ID):
    try:
        current_datetime = request.args.get("current_datetime")
        if current_datetime:
            try:
                current_datetime_obj = datetime.fromisoformat(
                    current_datetime.replace("Z", "+00:00")
                )
                # SQLite-compatible format: "YYYY-MM-DD HH:MM:SS"
                current_datetime = current_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

            except ValueError:
                return jsonify({"success": False,"error": f"Invalid datetime format: {current_datetime}"}), 400

        batches = get_batch_of_completed_and_after_current_time(teacher_ID, current_datetime)
        return jsonify({"success": True, "batches": batches}), 200

    except Exception as e:
        print("Error in api_get_completed_batches:", e)
        return jsonify({"success": False, "error": str(e)}), 500

