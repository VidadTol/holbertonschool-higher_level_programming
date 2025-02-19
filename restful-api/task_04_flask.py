#!/usr/bin/env python3

"""
Simple Flask API

This script creates a basic Flask API server.
It handles GET and POST requests and responds with plain text or JSON data
depending on the endpoint.
"""


from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """ respond with a welcome message """
    return "Welcome to the Flask API"


@app.route("/data")
def list_users():
    """ respond with a username """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """ respond with a status message """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """ respond with user data """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """ add a new user """
    user_data = request.get_json()

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400
    users[user_data["username"]] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
