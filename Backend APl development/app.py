from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join("data", "projects.json")


def load_projects():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_projects(projects):
    with open(DATA_FILE, "w") as file:
        json.dump(projects, file, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/projects", methods=["GET"])
def get_projects():
    projects = load_projects()

    return jsonify({
        "success": True,
        "count": len(projects),
        "projects": projects
    })


@app.route("/api/projects", methods=["POST"])
def add_project():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required"
        }), 400

    name = data.get("name")
    description = data.get("description")
    technology = data.get("technology")

    if not name or not description or not technology:
        return jsonify({
            "success": False,
            "message": "name, description and technology are required"
        }), 400

    projects = load_projects()

    new_project = {
        "id": len(projects) + 1,
        "name": name,
        "description": description,
        "technology": technology
    }

    projects.append(new_project)
    save_projects(projects)

    return jsonify({
        "success": True,
        "message": "Project added successfully",
        "project": new_project
    }), 201


if __name__ == "__main__":
    app.run(debug=True)