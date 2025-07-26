from flask import Blueprint, request, jsonify
from .subcoord_queries import add_sub_to_volunteers_in_school

subcoord_bp = Blueprint("subcoord_bp", __name__)

@subcoord_bp.route("/api/substitute_coordinator/<teacher_ID>/add_substitute_to_list", methods=["POST"])
def add_substitute_to_list(teacher_ID):
    data = request.json
    substitute_ID = data.get("substitute_ID")
    result = add_sub_to_volunteers_in_school(teacher_ID, substitute_ID)

    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200
