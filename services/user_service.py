from datetime import datetime, timedelta, timezone
from os import getenv
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from repository.user_repository import UserRepository
from passlib.context import CryptContext
import jwt

from schemas.token_schema import TokenData
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserService:
    async def get_user_by_username(username: str):
        return await UserRepository.get_user_by_username(username)
     
    async def authenticate_user(username: str, password: str):
        user = await UserRepository.get_user_by_username(username)
        if not user:
            return False
        if not pwd_context.verify(password, user.senha):
            return False
        return user

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=1)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, getenv('SECRET_KEY'), algorithm=getenv('ALGORITHM'))
        return encoded_jwt
    
    async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não foi possível validar suas credentiais. Tente fazer login novamente.",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, getenv('SECRET_KEY'), algorithms=getenv('ALGORITHM'))
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except jwt.InvalidTokenError:
            raise credentials_exception
        user = await UserRepository.get_user_by_username(token_data.username)
        if user is None:
            raise credentials_exception
        return user
    