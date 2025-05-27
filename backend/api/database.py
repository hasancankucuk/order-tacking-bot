from flask import Blueprint, jsonify, request  # type: ignore
from helpers.path_checker import get_validated_db_path
from db.methods import delete_database, seed_database
from db.db_utils import create_db

db_bp = Blueprint("database", __name__)

@db_bp.route("/api/database/delete", methods=["DELETE"])
def drop_database():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404

    try:
        success = delete_database(db_path)
        if success:
            create_db()
            return jsonify({"message": "All tables dropped successfully", "code": 200}), 200
        else:
            return jsonify({"error": "Failed to drop tables", "code": 500}), 500
    except Exception as e:
        return jsonify({"error": f"Failed to drop tables: {str(e)}", "code": 500}), 500


@db_bp.route("/api/database/seed", methods=["POST"])
def seed_db():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404

    data = request.get_json()
    role = data.get("role")
    try:
        if role != "admin":
            return jsonify({"error": "Only admin can seed the database", "code": 403}), 403
        
        success = seed_database(db_path)
        if success:
            return jsonify({"message": "Seeded successfully", "code": 200}), 200
        else:
            return jsonify({"error": "Failed to seed", "code": 500}), 500
    except Exception as e:
        return jsonify({"error": f"Failed to drop tables: {str(e)}", "code": 500}), 500