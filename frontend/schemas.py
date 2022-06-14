from pydantic import BaseModel


class User(BaseModel):
    uid: int
    name: str


class Role(BaseModel):
    uid: int
    name: str
