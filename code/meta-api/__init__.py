import os
import sys
from flask import Flask, jsonify, make_response, request
from .controllers import fetchController


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return "Hello, World!"

    @app.route('/', methods=['POST'])
    def fetch():
        url = request.form.get('url')
        if url:
            return jsonify(fetchController.fetch_meta(url))
        else:
            return make_response(jsonify({'error': 'url not provided'}), 400)

    return app
