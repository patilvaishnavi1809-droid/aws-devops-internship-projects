"""
Minimal Flask application used to demonstrate the Docker -> ECR -> Jenkins ->
Lambda pipeline. Not meant to be complex - the point of this project is the
CI/CD pipeline around it.
"""
from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from the containerized app!",
        "timestamp": datetime.datetime.utcnow().isoformat()
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
