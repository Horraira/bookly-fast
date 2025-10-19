from fastapi import APIRouter, HTTPException, status, Depends
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from src.db.main import get_session
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)) -> list[Book]:
    books = await book_service.get_all_book(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book


@book_router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@book_router.patch("/{book_id}")
async def update_book(book_id: int, updated_book: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            if updated_book.title is not None:
                book["title"] = updated_book.title
            if updated_book.author is not None:
                book["author"] = updated_book.author
            if updated_book.publisher is not None:
                book["publisher"] = updated_book.publisher
            if updated_book.pages is not None:
                book["pages"] = updated_book.pages
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@book_router.delete("/{book_id}")
async def delete_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
