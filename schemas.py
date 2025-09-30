from typing import List
from pydantic import  BaseModel,Field

class BookCreate(BaseModel):
    title:str=Field(min_length=1,max_length=200)
    pages:int=Field(ge=1)
    author_id:int

class BookOut(BaseModel):
    id: int
    title: str
    pages: int
    author_id: int
    class Config:
        from_attributes=True

class AuthorCreate(BaseModel):
    name:str=Field(min_length=1,max_length=120)

class AuthorOut(BaseModel):
    id: int
    name: str
    #nested :return books with author
    books: List[BookOut]=[]
    class Config:
        from_attributes=True