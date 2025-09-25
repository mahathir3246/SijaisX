from flask import Blueprint, request, jsonify
from .delete_assignments_query import delete_assignments_query

delete_assignments_bp = Blueprint("delete_assignments_bp", __name__)

@delete_assignments_bp.route("/delete_assignments", methods=["POST"])
def delete_assignments():
    data = request.json
    assignment_ids = data.get("assignment_ids", [])

    result = delete_assignments_query(assignment_ids)
    return jsonify(result)