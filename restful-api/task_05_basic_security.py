#!/usr/bin/env python3
"""
Basic Security with Flask

This script creates a basic Flask API server with basic authentication and JWT-based authentication.
It handles GET and POST requests and responds with plain text or JSON data depending on the endpoint.

"""

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

users = {"user1":{"username":"user1", "password":generate_password_hash("password1"), "role":"user"},
"admin1":{"username":"admin1", "password":generate_password_hash("password1"), "role":"admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None

@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        return jsonify({'error': 'Missing arguments'}), 400

    if username in users and check_password_hash(users.get(username), password):
        access_token = create_access_token(identity=username)
        return jsonify({'message': 'Login successful', 'access_token': access_token})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({'message': 'JWT Auth: Access Granted'})

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin_only():
    log_user= get_jwt_identity()

    if log_user not in users:
        return jsonify({'error': 'User not found'}), 404
    
    if users[log_user]["role"] != 'admin':
        return jsonify({'error': 'Admin access required'}), 403
    return jsonify({'message': 'Admin access granted'})

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
