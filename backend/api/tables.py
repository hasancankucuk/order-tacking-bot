from flask import Blueprint, jsonify # type: ignore
from db.methods import get_tables, get_all_from_table
from helpers.path_checker import get_validated_db_path


tables_bp = Blueprint("tables", __name__)

@tables_bp.route("/api/tables")
def get_tables_route():
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404
    tables = get_tables(db_path)
    return jsonify(tables)

@tables_bp.route("/api/tables/<table_name>")
def get_table_route(table_name):
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404
    tables = get_tables(db_path)
    if table_name not in tables:
        return jsonify({"error": f"Table '{table_name}' not found.", "code": 404}), 404
    
    result = get_all_from_table(table_name, db_path)
    if result is None:
        return jsonify({"error": f"Failed to retrieve data from table '{table_name}'." ,"code": 500}), 500
    return jsonify({table_name: result})