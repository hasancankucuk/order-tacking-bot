import requests
from flask import Blueprint, jsonify, request

manuel_tests_bp = Blueprint("manuel_tests", __name__)

@manuel_tests_bp.route("/api/test/manuel/nlu", methods=["POST"])
def run_nlu_test():
    try:
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "Missing input text.", "code": 400}), 400

        response = requests.post( "http://localhost:5005/model/parse", json={"text": text} )
        if response.status_code != 200:
            return jsonify({"error": "Rasa NLU parse failed", "code": 500}), 500

        result = response.json()
        expected_intent = data.get("expected_intent")
        if expected_intent:
            assert result["intent"]["name"] == expected_intent, (
                f"Expected intent '{expected_intent}', but got '{result['intent']['name']}'"
            )

        return jsonify({
            "text": text,
            "intent": result["intent"]["name"],
            "entities": result["entities"],
            "confidence": result["intent"]["confidence"]
        }), 200

    except AssertionError as ae:
        return jsonify({"error": str(ae), "code": 400}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to run NLU test: {str(e)}", "code": 500}), 500