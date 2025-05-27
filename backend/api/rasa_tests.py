import json
import os
import yaml
import subprocess
from flask import jsonify, Blueprint, send_from_directory

test_bp = Blueprint("rasa_tests", __name__)


@test_bp.route("/api/test/health", methods=["GET"])
def test_health():
    return jsonify({"status": "ok"}), 200

@test_bp.route("/api/test/core", methods=["GET"])
def test_core():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Şu anki dosya dizini
        backend_path = os.path.join(base_dir, "backend")

        results = subprocess.run(
            ["rasa", "test", "core", "--stories", "data", "--model", "models"],
            cwd=backend_path,
            capture_output=True,
            text=True,
            check=True,
        )

        # failed_stories_path = os.path.join(base_path, "failed_test_stories.yml")
        # report_path = os.path.join(base_path, "TEDPolicy_report.json")
        # story_report_path = os.path.join(base_path, "story_report.json")

        # with open(report_path, "r") as f:
        #     report = json.load(f)

        # with open(failed_stories_path, "r") as f:
        #     failed_stories = yaml.safe_load(f)

        # with open(story_report_path, "r") as f:
        #     story_report = json.load(f)

        return (
            jsonify(
                {
                    "message": "Core test completed",
                    # "report": report,
                    # "failed_stories": failed_stories,
                    # "story_report": story_report,
                    # "results": {
                    #     "story_confusion_matrix": os.path.join(
                    #         base_path, "story_confusion_matrix.png"),
                    #     "TEDPolicy_confusion_matrix": os.path.join(
                    #         base_path, "TEDPolicy_confusion_matrix.png"),
                    # },
                    "code": 200,
                }
            ),
            200,
        )

    except subprocess.CalledProcessError as e:
        return (
            jsonify({"error": "Rasa test failed", "code": 500}),
            500,
        )

    except FileNotFoundError as e:
        return jsonify({"error": f"{e.filename} not found", "code": 500}), 500

@test_bp.route("/api/test/nlu", methods=["GET"])
def test_nlu():
    try:
        if os.getcwd() == "/app":
            subprocess.run(
                ["rasa", "test", "nlu", "--nlu", "data/nlu.yml", "--out", "results"],
                capture_output=True,
                text=True,
                check=True,
            )
            base_path = "results"
        else:
            subprocess.run(
                ["rasa", "test", "nlu", "--nlu", "data/nlu.yml", "--out", "results"],
                cwd="backend",
                capture_output=True,
                text=True,
                check=True,
            )
            base_path = os.path.join("backend", "results")

        report_path = os.path.join(base_path, "DIETClassifier_report.json")
        errors_path = os.path.join(base_path, "DIETClassifier_errors.json")

        with open(report_path, "r") as f:
            report = json.load(f)

        with open(errors_path, "r") as f:
            errors = json.load(f)

        return (
            jsonify(
                {
                    "message": "Core test completed",
                    "report": report,
                    "errors": errors,
                    "results": {
                        "confusion_matrix_image": os.path.join(
                            base_path, "DIETClassifier_confusion_matrix.png"),
                        "histogram_image": os.path.join(
                            base_path, "DIETClassifier_histogram.png"),
                    },
                    "code": 200,
                }
            ),
            200,
        )

    except subprocess.CalledProcessError as e:
        return (
            jsonify({"error": "Rasa test failed", "code": 500}),
            500,
        )

    except FileNotFoundError as e:
        return jsonify({"error": f"{e.filename} not found", "code": 500}), 500

RESULTS_DIR = os.path.abspath("backend/results")

@test_bp.route("/backend/results/<path:filename>", methods=["GET"])
def serve_result_file(filename):
    return send_from_directory(RESULTS_DIR, filename)