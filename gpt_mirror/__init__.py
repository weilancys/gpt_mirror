from flask import Flask, redirect, url_for
from . import chatgpt
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    # config
    # https://flask.palletsprojects.com/en/2.2.x/config/#instance-folders
    app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(chatgpt.bp, url_prefix='/chatgpt')
    @app.route('/')
    def index():
        return redirect(url_for('chatgpt.chat'))
    
    return app