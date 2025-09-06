
from fastapi import APIRouter, HTTPException, status
from data import books, Book
from book_schemes import Update_book_model
from db_connection import get_connection

book_router = APIRouter(prefix="/books")


# get all books
@book_router.get("/")
def books():

   conn = get_connection()
   cur = conn.cursor(dictionary=True)

   sql = "SELECT * FROM books"
   cur.execute(sql)

   rows = cur.fetchall()
   conn.close()

   return rows
   

#  get specific book
@book_router.get("/{book_id}")
def get_spcific_book(book_id: int):
    conn = get_connection()

    cur = conn.cursor(dictionary=True)
    sql = "SELECT title, author, page_count, published_at FROM books WHERE id = %s"
    cur.execute(sql,(book_id,))

    row = cur.fetchone()
    conn.close()

    return row


# creating book
@book_router.post("/")
def creating_book(load_data: Book):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    sql = "INSERT INTO books (title, author, page_count, published_at) VALUES (%s, %s, %s, %s)"

    cur.execute(sql, (load_data.title, load_data.author, load_data.page_count, load_data.published_at))
    conn.commit()

    row_id = cur.lastrowid
    sql_read = "SELECT title, author, page_count, published_at FROM books WHERE id = %s"
    cur.execute(sql_read, (row_id,))

    row = cur.fetchone()
    conn.close()

    return row



@book_router.put("/{book_id}", response_model=Update_book_model)
def update_book(book_id: int, load_data: Book):

    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    read_sql = "SELECT * FROM books WHERE id= %s"
    cur.execute(read_sql, (book_id,))

    exists = cur.fetchone()
    if not exists:
      raise  HTTPException(status_code=404, detail="Book Not Found!")
   
    sql = "UPDATE books SET title = %s, author = %s, page_count = %s, published_at = %s WHERE id = %s"
    cur.execute(sql, (load_data.title, load_data.author, load_data.page_count, load_data.published_at, book_id))
    conn.commit()

    conn.close()
   

        
    return {
        "title": load_data.title,
        "author": load_data.author,
        "page_count": load_data.page_count,
        "published_at": load_data.published_at,
    }
        



@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    conn = get_connection()

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id=%s",(book_id,))

    exists = cursor.fetchone()
    if not exists:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    cursor.execute("DELETE FROM books WHERE id= %s", (book_id,))
    conn.commit()

    return None
