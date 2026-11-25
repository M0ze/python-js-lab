# app.py — Flask notes app (Python/JS P1)

# A tiny note-taking app with a vanilla JS frontend. No database yet — just
# an in-memory store to learn routing + templates + JSON APIs.

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

NOTES = []
NEXT_ID = 1

STATIC_DIR = Path(__file__).parent / "static"
TEMPLATES_DIR = Path(__file__).parent / "templates"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(NOTES)


@app.route("/api/notes", methods=["POST"])
def create_note():
    global NEXT_ID
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "text is required"}), 400
    note = {
        "id": NEXT_ID,
        "text": text,
        "created": datetime.now(timezone.utc).isoformat(),
    }
    NEXT_ID += 1
    NOTES.append(note)
    return jsonify(note), 201


@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    global NOTES
    match = [n for n in NOTES if n["id"] == note_id]
    if not match:
        return jsonify({"error": "not found"}), 404
    NOTES = [n for n in NOTES if n["id"] != note_id]
    return "", 204


@app.route("/api/notes/<int:note_id>", methods=["PATCH"])
def patch_note(note_id):
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    for note in NOTES:
        if note["id"] == note_id:
            if text:
                note["text"] = text
            return jsonify(note)
    return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
