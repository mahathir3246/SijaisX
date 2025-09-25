from flask import Blueprint, request, jsonify
from .delete_query import delete_assignments_query, is_subcoord

delete_bp = Blueprint("delete_bp", __name__)

@delete_bp.route("/assignments/delete", methods=["DELETE"])
def delete_assignments():
    data = request.json
    assignment_ids = data.get("assignment_ids", [])
    teacher_ID = data.get("teacher_ID")

    if not teacher_ID:
        return jsonify({"success": False, "error": "teacher_ID is required"}), 400

    if not assignment_ids:
        return jsonify({"success": False, "error": "No assignment_ids provided"}), 400

    subcoord_flag = is_subcoord(teacher_ID)
    result = delete_assignments_query(assignment_ids, teacher_ID, is_subcoord=subcoord_flag)
    return jsonify(result)
