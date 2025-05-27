from flask import Blueprint, jsonify, request  # type: ignore
from helpers.path_checker import get_validated_db_path
from db.methods import get_user, set_user, update_user, get_tables
from db.db_utils import create_db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found."}), 404

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required", "code": 400}), 400

    user = get_user(username, password, db_path)
    if user:
        return jsonify({"message": "Login successful", "user": user, "code": 200}), 200
    else:
        return jsonify({"error": "Invalid credentials", "code": 401}), 401


@auth_bp.route("/api/auth/register", methods=["POST"])
def register():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    role = data.get("role", "user")

    if not username or not password or not email or not role:
        return jsonify({"error": "All fields are required"}), 400
    
    if get_tables(db_path) is None:
        create_db()
    success = set_user(username, password, email, role, db_path)
    if success:
        return jsonify({"message": "User registered successfully", "code": 201}), 201
    else:
        return jsonify({"error": "Registration failed", "code": 500}), 500
    
@auth_bp.route("/api/auth/update", methods=["PUT"])
def update():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found."}), 404

    print(f"Updating user with ID:")
    data = request.get_json()
    user_id = data.get("id")
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    role = data.get("role")

    success = update_user(user_id, username, password, email, role, db_path)
    if success:
        return jsonify({"message": "User updated successfully", "code": 200}), 200
    else:
        return jsonify({"error": "Update failed", "code": 500}), 500