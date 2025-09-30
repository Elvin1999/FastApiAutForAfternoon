from datetime import datetime,timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import jwt,JWTError

SECRET_KEY="CHANGE_ME______STRONG_SECRET"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(raw:str,hashed:str):
    return pwd_context.verify(raw,hashed)

def create_access_token(sub:str,role:str,expires_minutes:int=ACCESS_TOKEN_EXPIRE_MINUTES):
    now=datetime.utcnow()
    payload={
        'sub': sub,
        'role': role,
        'iat': now,
        'exp': now + timedelta(minutes=expires_minutes)
    }

    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])