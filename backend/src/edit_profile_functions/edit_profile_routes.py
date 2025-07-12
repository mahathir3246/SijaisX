from flask import Blueprint, request, jsonify
from edit_profile_queries import update_teacher_profile, update_substitute_profile

edit_profile_bp = Blueprint("edit_profile_bp", __name__)

@edit_profile_bp.route("/api/edit_profile/substitute/<string:substitute_ID>", methods=["PATCH"])
def edit_substitute_profile(substitute_ID):
    data = request.json
    name = data.get("name")
    phone_number = data.get("phone_number")
    email = data.get("email")
    password = data.get("password")
    experience = data.get("experience")
    highest_education = data.get("highest_education")

    result = update_substitute_profile(substitute_ID, name, phone_number, email, password,
                                       experience, highest_education)
    
    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200

@edit_profile_bp.route("api/edit_profile/teacher/<string:teacher_ID>", methods=["PATCH"])
def edit_teacher_profile(teacher_ID):
    data = request.json
    name = data.get("name")
    phone_number = data.get("phone_number")
    email = data.get("email")
    password = data.get("password")

    result = update_teacher_profile(teacher_ID, name, phone_number, email, password)

    if not result["success"]:
        return jsonify(result), 400
    return jsonify(result), 200
