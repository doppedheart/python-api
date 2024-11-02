from flask import jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

def handle_different_error(e):
    """Handle non-HTTP exceptions."""
    response = {
        "error": "An unexpected error occurred",
        "message": str(e)
    }
    return jsonify(response), 500

def handle_integrity_error(e):
    """Handle database integrity errors."""
    response = {
        "error": "Integrity Error",
        "message": "A unique constraint or integrity violation occurred"
    }
    return jsonify(response), 400

def handle_http_exception(e):
    """Handle HTTP exceptions."""
    response = {
        "error": e.name,
        "message": e.description
    }
    return jsonify(response), e.code

def register_error_handlers(app):
    """Register error handlers with the Flask app."""
    app.register_error_handler(Exception, handle_different_error)
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(IntegrityError, handle_integrity_error)
