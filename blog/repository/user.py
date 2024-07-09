from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from blog.schemas import schemas
from blog.database import models
from blog.utils import hashing


def create_user(request: schemas.CreateUser, db: Session):
    hashed_password = hashing.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')

    return user
