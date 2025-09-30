from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

# Models
class Author(Base):
    __tablename__="authors"
    id = Column(Integer,primary_key=True)
    name = Column(String(120),unique=True,nullable=False)
    books=relationship("Book",back_populates="author",cascade="all, delete-orphan")

class Book(Base):
    __tablename__="books"
    id = Column(Integer,primary_key=True)
    title = Column(String(200),nullable=False)
    pages = Column(Integer,nullable=False,default=1)
    author_id = Column(Integer,ForeignKey("authors.id"),nullable=False)
    author = relationship("Author",back_populates="books")