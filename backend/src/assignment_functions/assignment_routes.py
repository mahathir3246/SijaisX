from flask import Blueprint, request, jsonify
from .assignment_queries import volunteer_for_assignment, update_assignment_status, get_assignment_volunteers

assignment_bp = Blueprint("assignment_bp", __name__)

@assignment_bp.route("/api/assignments/<assignment_ID>/volunteer", methods=["POST"])
def volunteer(assignment_ID):
    data = request.json
    substitute_ID = data.get("substitute_ID")
    result = volunteer_for_assignment(substitute_ID, assignment_ID)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@assignment_bp.route("/api/assignments/<assignment_ID>/status", methods=["PATCH"])
def update_status(assignment_ID):
    data = request.json
    teacher_ID = data.get("teacher_ID")
    new_status = data.get("status")
    substitute_ID = data.get("substitute_ID")
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
