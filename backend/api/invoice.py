from flask import Blueprint, send_from_directory # type: ignore
import os

invoice_bp = Blueprint("invoice", __name__)

@invoice_bp.route("/invoice/<path:filename>", methods=["GET"])
def serve_invoice(filename):
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    invoice_dir = os.path.join(backend_dir, "invoice")
    return send_from_directory(invoice_dir, filename)
