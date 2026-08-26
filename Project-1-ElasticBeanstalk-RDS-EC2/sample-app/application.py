"""
Sample Flask application for AWS Elastic Beanstalk deployment.
Elastic Beanstalk (Python platform) looks for a WSGI callable named
'application' by default -- this file follows that convention.
"""
from flask import Flask, jsonify
import os

application = Flask(__name__)


@application.route("/")
def home():
    return jsonify({
        "message": "Hello from Elastic Beanstalk!",
        "status": "running",
        "environment": os.environ.get("RDS_HOSTNAME", "RDS not connected yet")
    })


@application.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
