from fastapi import FastAPI
from routes import book_router
from data import books


app =  FastAPI()

app.include_router(book_router)