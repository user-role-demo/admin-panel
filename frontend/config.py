import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    backend_url: str
    app_host: str
    app_port: str
    debug: bool
    secret_key: str


def load_from_env() -> AppConfig:
    return AppConfig(
        backend_url=os.environ['BACKEND_URL'],
        app_host=os.environ['APP_HOST'],
        app_port=os.environ['APP_PORT'],
        debug=os.getenv('DEBUG', 'False'),
        secret_key=os.environ['SECRET_KEY'],
    )


app_config = load_from_env()
