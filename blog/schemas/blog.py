from __future__ import annotations
from pydantic import BaseModel


class BaseBlog(BaseModel):
    title: str
    body: str


class Blog(BaseBlog):
    id: int


class CreateBlog(BaseBlog):
    pass


class ShowBlog(BaseBlog):
    id: int

    creator: User


from blog.schemas.user import User

ShowBlog.update_forward_refs()
