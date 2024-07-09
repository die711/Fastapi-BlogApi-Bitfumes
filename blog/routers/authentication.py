from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from blog.database import models, database
from blog.auth import token
from blog.utils import hashing
from sqlalchemy.orm import Session
from blog.schemas import schemas

router = APIRouter(
    tags=['Authentication'],
)


@router.post('/login', response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials')

    if not hashing.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')

    # generate auth token and return
    access_token = token.create_access_token(
        data={'sub': user.email}
    )

    return schemas.Token(access_token=access_token, token_type='bearer')
