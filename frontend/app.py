from flask import Flask

from frontend.config import app_config
from frontend.views import index


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = app_config.secret_key
    app.register_blueprint(index.view)

    return app
