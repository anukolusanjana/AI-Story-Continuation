import os
from flask import Flask, jsonify, request
from model import generate_story

app = Flask(__name__)

@app.get("/ping")
def ping():
    return jsonify({"status": "ok"})

@app.post("/invocations")
def invocations():
    payload = request.get_json(silent=True) or {}
    try:
        result = generate_story(
            payload.get("prompt", ""),
            payload.get("max_new_tokens", 60),
            payload.get("temperature", 0.8),
        )
        return jsonify({"generated_text": result})
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception:
        app.logger.exception("Inference failed")
        return jsonify({"error": "Model inference failed"}), 500
