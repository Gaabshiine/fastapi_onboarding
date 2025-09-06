from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    page_count: int
    published_at: Optional[date] = None


class Update_book_model(BaseModel):
    title: str
    author: str
    page_count: int





