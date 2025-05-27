from flask import Blueprint, request, jsonify # type: ignore
from db.methods import get_custom_query, create_connection, get_all_from_table
from helpers.path_checker import get_validated_db_path
from helpers.extract_table_name import extract_table_name

custom_query_bp = Blueprint("custom_query", __name__)

@custom_query_bp.route("/api/custom_query", methods=["POST"])
def custom_query_post():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided", "code": 400}), 400
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404
    result = get_custom_query(query, db_path=db_path)
    if result is None:
        return jsonify({"error": "Query failed", "code": 500}), 500
    return jsonify({"table": result})


@custom_query_bp.route("/api/custom_query", methods=["GET"])
def custom_query_get():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "No query provided", "code": 400}), 400
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404
    result = get_custom_query(query, db_path=db_path)
    if result is None:
        return jsonify({"error": "Query failed", "code": 500}), 500
    return jsonify({"table": result})


@custom_query_bp.route("/api/custom_query", methods=["PUT"])
def custom_query_update():
    data = request.get_json()
    query = data.get("query")
    params = data.get("params")
    if not query:
        return jsonify({"error": "No query provided", "code": 400}), 400
    db_path = get_validated_db_path()
    if not db_path:
        return jsonify({"error": "Database not found.", "code": 404}), 404
    conn = create_connection(db_path)
    try:
        cur = conn.cursor()

        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
        table_name = extract_table_name(query)
        result = get_all_from_table(table_name, db_path)

        if result is None:
            return jsonify({"error": True, "rowcount": cur.rowcount , "code": 500 }), 500
        
        return jsonify({"success": True, "table": result , "code": 200 }), 200
    except Exception as e:
        return jsonify({"error": str(e), "code": 500}), 500
    finally:
        conn.close()
