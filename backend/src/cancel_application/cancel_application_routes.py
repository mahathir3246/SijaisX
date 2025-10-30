from flask import Blueprint, request, jsonify
from .cancel_application_queries import *

cancel_application_bp = Blueprint("cancel_application_bp", __name__)

@cancel_application_bp.route("/api/cancel_accepted_batch_application", methods=["POST"])
def cancel_accepted_batch_application():
    data = request.json
    substitute_ID = data.get("substitute_ID")
    batch_ID = data.get("batch_ID")
    result = cancel_confirmed_application_for_batch(substitute_ID, batch_ID)
    return jsonify(result)
