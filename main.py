from fastapi import FastAPI
from routes import book_router
from data import books
from db_connection import get_connection


app =  FastAPI()

# @app.on_event("startup")
# def startup():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             title VARCHAR(200) NOT NULL,
#             author VARCHAR(200) NOT NULL,
#             page_count INT NOT NULL,
#             published_at DATE NULL
#         )
#     """)
#     conn.commit()
#     conn.close()


app.include_router(book_router)



