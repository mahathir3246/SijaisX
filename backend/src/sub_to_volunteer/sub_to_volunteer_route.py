from flask import Blueprint, request, jsonify
from .sub_to_school_list import add_to_school_list
from .sub_to_assignment_list import add_to_assignment_list

sub_to_list_bp = Blueprint("sub_to_list_bp", __name__)

@sub_to_list_bp.route("/api/sub_to_school_list", methods=["POST"])
def add_sub_to_school_list():
    data = request.json
    teacher_ID = data.get("teacher_ID")
    substitute_ID = data.get("substitute_ID")

    if not teacher_ID or not substitute_ID:
        return jsonify({"success": False, "message": "Missing required fields"}), 400

    result = add_to_school_list(teacher_ID, substitute_ID)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@sub_to_list_bp.route("/api/sub_to_assignment_list", methods=["POST"])
def add_sub_to_assignment_list():
    data = request.json
    substitute_ID = data.get("substitute_ID")
    assignment_ID = data.get("assignment_ID")

    if not substitute_ID or not assignment_ID:
        return jsonify({"success": False, "message": "Missing required fields"}), 400

    result = add_to_assignment_list(substitute_ID, assignment_ID)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

