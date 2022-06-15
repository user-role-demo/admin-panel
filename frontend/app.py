from flask import Flask

from frontend.config import app_config
from frontend.views import index, role, user


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = app_config.secret_key

    app.register_blueprint(index.view)
    app.register_blueprint(role.view, url_prefix='/roles')
    app.register_blueprint(user.view, url_prefix='/users')

    return app
