from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from blog.schemas.token import TokenData
from blog.auth.token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def get_current_user(token: str = Depends(oauth2_scheme)) -> TokenData:
    return verify_token(token)
