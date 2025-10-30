from flask import Blueprint, request, jsonify
from .cancel_application_queries import *

cancel_application_bp = Blueprint("cancel_application_bp", __name__)

@cancel_application_bp.route("/api/cancel_accepted_batch_application", methods=["POST"])
def cancel_accepted_batch_application():
    data = request.json
    substitute_ID = data.get("substitute_ID")
    batch_ID = data.get("batch_ID")
    if not substitute_ID or not batch_ID:
        return jsonify({"success": False, "error": "substitute_ID and batch_ID are required"}), 400
    result = cancel_confirmed_application_for_batch(substitute_ID, batch_ID)
    return jsonify(result)
