from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt(password: str) -> str:
    return pwd_ctx.hash(password)


def verify(hashed_password: str, plain_password: str) -> bool:
    return pwd_ctx.verify(plain_password, hashed_password)
