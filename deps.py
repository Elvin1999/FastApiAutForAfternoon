from fastapi import HTTPException,Depends,status
from sqlalchemy.orm import Session
from database import  SessionLocal

def get_db():
    db:Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()