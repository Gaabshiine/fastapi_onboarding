
from fastapi import APIRouter, HTTPException, status
from data import books, Book
from book_schemes import Update_book_model

book_router = APIRouter(prefix="/books")


# get all books
@book_router.get("/")
def all_books():
    return books


#  get specific book
@book_router.get("/{book_id}")
def get_spcific_book(book_id: int):

    for book in books:         
        if book.id == book_id:   
            return book
    
    raise HTTPException(status_code=404, detail="Book not found")


# creating book
@book_router.post("/")
def creating_book(load_data: Book):

    books.append(load_data)

    return load_data



@book_router.put("/{book_id}", response_model=Update_book_model)
def update_book(book_id: int, load_data: Book):

    for book in books:
        if book.id == book_id:
            book.id = load_data.id
            book.title = load_data.title
            book.author = load_data.author
            book.published_at = load_data.published_at
        
        if not book:
            raise HTTPException(status_code=404, detail="Book Not found")
        
    return book
        



@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    global books
    

    # value_if_true if condition else value_if_false
    new_books = [b_ for b_ in books if b_.id != book_id]

    books = new_books
    return None
