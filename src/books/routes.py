from fastapi import APIRouter, HTTPException, status, Depends
from src.books.schemas import Book, BookUpdateModel, BookCreateModel
from src.db.main import get_session
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession

book_router = APIRouter()
book_service = BookService()

BOOK_NOT_FOUND_MSG = "Book not found"


@book_router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)) -> list[Book]:
    books = await book_service.get_all_book(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book


@book_router.get("/{book_uid}", status_code=status.HTTP_200_OK, response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    else:
        raise HTTPException(status_code=404, detail=BOOK_NOT_FOUND_MSG)


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=BOOK_NOT_FOUND_MSG
        )
    return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_200_OK)
async def delete_book(
    book_uid: str, session: AsyncSession = Depends(get_session)
) -> dict:
    deleted = await book_service.delete_book(book_uid, session)
    if deleted:
        return {"message": "Book deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=BOOK_NOT_FOUND_MSG
    )
