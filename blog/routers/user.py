from fastapi import APIRouter, Depends
from blog.database import database
from blog.schemas.user import CreateUser, ShowUser
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users'],
)

get_db = database.get_db


@router.post('/', response_model=ShowUser)
def create_user(request: CreateUser, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
