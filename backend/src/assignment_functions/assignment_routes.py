from flask import Blueprint, request, jsonify
from .assignment_queries import volunteer_for_assignment, update_assignment_status, get_assignment_volunteers, create_batch_assignment

assignment_bp = Blueprint("assignment_bp", __name__)

@assignment_bp.route("/api/assignments/<assignment_ID>/volunteer", methods=["POST"])
def volunteer(assignment_ID):
    data = request.json
    substitute_ID = data.get("substitute_ID")

    # check
    if not substitute_ID:
        return jsonify({"success": False, "error": "substitute_ID is required"}), 400

    result = volunteer_for_assignment(substitute_ID, assignment_ID)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@assignment_bp.route("/api/assignments/<assignment_ID>/status", methods=["PATCH"])
def update_status(assignment_ID):
    data = request.json
    teacher_ID = data.get("teacher_ID")
    new_status = data.get("status")
    substitute_ID = data.get("substitute_ID")  # May be None if not accepting

    # check
    if not teacher_ID:
        return jsonify({"success": False, "error": "teacher_ID is required"}), 400
    if not new_status:
        return jsonify({"success": False, "error": "status is required"}), 400

    # Extra check
    if new_status == "accepted" and not substitute_ID:
        return jsonify({"success": False, "error": "substitute_ID is required for accepting"}), 400

    result = update_assignment_status(assignment_ID, teacher_ID, new_status, substitute_ID)

    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200


@assignment_bp.route("/api/assignments/<assignment_ID>/volunteers", methods=["GET"])
def get_volunteers(assignment_ID):
    result = get_assignment_volunteers(assignment_ID)
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200


@assignment_bp.route("/api/assignments/create_batch", methods=["POST"])
def create_batch():
    data = request.json
    teacher_ID = data.get("teacher_ID")
    assignments = data.get("assignments", [])
    result = create_batch_assignment(teacher_ID, assignments)

    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200
