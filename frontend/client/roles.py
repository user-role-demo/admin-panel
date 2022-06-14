import httpx

from frontend.schemas import Role, User


class RolesClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/roles'

    def get_all(self) -> list[Role]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()

        roles = response.json()
        return [Role(**role) for role in roles]

    def get_by_id(self, uid: int) -> Role:
        response = httpx.get(f'{self.url}/{uid}')
        response.raise_for_status()

        payload = response.json()
        return Role(**payload)

    def get_users(self, uid: int) -> list[User]:
        response = httpx.get(f'{self.url}/{uid}/users')
        response.raise_for_status()

        users = response.json()
        return [User(**user) for user in users]
