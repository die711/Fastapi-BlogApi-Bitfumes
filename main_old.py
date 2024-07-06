from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs

    if published:
        return {'data': f'{limit} published blog list from the database'}
    else:
        return {'data': f'{limit} blog list from the database'}


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'all unpubished blogs'
    }


@app.get('/blog/{id}')
def show(id: int):
    return {
        'data': id

    }


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return limit

    return {
        'data': {1, 2, 3, 4, 5}
    }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blogs(request: Blog):
    return {
        'data': f'Blog is created with title as {request.title}'
    }


