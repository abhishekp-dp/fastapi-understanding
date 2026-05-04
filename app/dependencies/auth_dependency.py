from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer

from app.core.jwt_handler import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)): #here depends on oauth2_scheme and find the login url endpoint
    print(token)
    payload = decode_token(token) #Fetches the token from the method

    user_id = payload.get("user_id")  # From that user id fetches that who made the request for eg {
                                                                                                    #  "user_id": 7,
                                                                                        #  "role": "admin",
    print(user_id)                                                                                          #  "exp": 1710300000
                                                                                                    # }

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return payload