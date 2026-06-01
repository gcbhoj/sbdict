from flask import Blueprint, jsonify
from controller.user_controller import CreateUserController

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/add", methods=["POST"])
def add_user():

    controller = CreateUserController()

    response = controller.create_user()

    return jsonify(response), 201