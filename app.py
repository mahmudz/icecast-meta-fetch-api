from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from controllers import fetchController

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/", methods=["POST"])
def fetch():
    url = request.json.get("url")
    if url:
        return jsonify(fetchController.fetch_meta(url))
    else:
        return make_response(jsonify({"error": "url not provided"}), 400)
