from pydantic import BaseModel
from typing import List
from blog.schemas.blog import Blog


class UserBase(BaseModel):
    name: str
    email: str


class User(UserBase):
    id: int


class CreateUser(UserBase):
    password: str


class ShowUser(UserBase):
    id: int

    blogs: List[Blog]
