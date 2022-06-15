import httpx

from frontend.schemas import User, Role


class UsersClient:

    def __init__(self, url: str) -> None:
        self.url = f'{url}/users'

    def get_all(self) -> list[User]:
        response = httpx.get(f'{self.url}/')
        response.raise_for_status()

        users = response.json()
        return [User(**user) for user in users]

    def get_by_id(self, uid: int) -> User:
        response = httpx.get(f'{self.url}/{uid}')
        response.raise_for_status()

        payload = response.json()
        return User(**payload)

    def get_roles(self, uid: int) -> list[Role]:
        response = httpx.get(f'{self.url}/{uid}/roles')
        response.raise_for_status()

        roles = response.json()
        return [Role(**role) for role in roles]
