from jose import jwt
from app.core.config import settings

def create_access_token(data: dict):
    return jwt.encode(
        data,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )