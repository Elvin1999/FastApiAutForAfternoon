from fastapi import FastAPI
from database import Base,engine
from routers import authors_router,books_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title='FastAPI with JWT & Roles')
app.include_router(authors_router)
app.include_router(books_router)