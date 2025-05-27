from flask import Flask, send_from_directory # type: ignore
from flask_cors import CORS # type: ignore
import os
from .tables import tables_bp
from .custom_query import custom_query_bp
from .auth import auth_bp
from .database import db_bp
from .rasa_tests import test_bp
from .manuel_tests import manuel_tests_bp
from .invoice import invoice_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.register_blueprint(tables_bp)
app.register_blueprint(custom_query_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(db_bp)
app.register_blueprint(test_bp)
app.register_blueprint(manuel_tests_bp)
app.register_blueprint(invoice_bp)

def main():
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False, threaded=True)

if __name__ == '__main__':
    main()