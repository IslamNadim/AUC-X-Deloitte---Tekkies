import os
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.headers.get("x-api-key") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
