from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    publication_year: int
    pages: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    publication_year: int
    pages: int
    language: str


class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    pages: Optional[int] = None
