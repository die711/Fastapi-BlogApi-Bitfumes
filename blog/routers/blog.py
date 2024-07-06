from fastapi import APIRouter, Depends, status, Response
from typing import List
from blog.schemas.blog import ShowBlog, CreateBlog
from blog.schemas.token import TokenData
from blog.database import database
from sqlalchemy.orm import Session
from blog.repository import blog
from blog.auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db),
        token_data: TokenData = Depends(get_current_user)):
    print(token_data)
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: CreateBlog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: CreateBlog, db: Session = Depends(get_db)):
    # , current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    # ,current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.get('/{id}', status_code=200, response_model=ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    # ,current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
