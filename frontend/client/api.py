from frontend.config import app_config
from frontend.client.roles import RolesClient
from frontend.client.users import UsersClient


class ApiClient:

    def __init__(self, url: str) -> None:
        self.roles = RolesClient(url)
        self.users = UsersClient(url)


client = ApiClient(url=app_config.backend_url)
