from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    id: int


class CreateBlog(BlogBase):
    pass


class UserBase(BaseModel):
    name: str
    email: str


class User(UserBase):
    id: int


class CreateUser(UserBase):
    password: str


class ShowUser(UserBase):
    id: int

    blogs = List[Blog]


class ShowBlog(BlogBase):
    id: int

    # creator: User


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

