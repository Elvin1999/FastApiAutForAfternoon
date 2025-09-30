from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from deps import get_db
from models import Book,Author
from schemas import BookCreate,BookOut

router = APIRouter(prefix="/api/books", tags=["books"])

@router.post("/",response_model=BookOut,status_code=201)
def create_book(payload:BookCreate,db:Session=Depends(get_db)):
    if not db.query(Author).get(payload.author_id):
        raise HTTPException(status_code=404,detail="Author not found")
    book=Book(title=payload.title.strip(),pages=payload.pages,author_id=payload.author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return BookOut.from_orm(book)

