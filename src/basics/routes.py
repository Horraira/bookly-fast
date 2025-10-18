from fastapi import Header, APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}


@router.get("/greet/{age}")
async def greet_name(
    name: str,
    city: Optional[str] = "Dhaka",
    age: int = 18,
) -> dict:
    if city:
        return {
            "message": f"Hello, {name}! You are {age} years old and live in {city}."
        }
    return {"message": f"Hello, {name}! You are {age} years old."}


class BookCreateModel(BaseModel):
    title: str
    author: str


@router.post("/create_book")
async def create_book(book_data: BookCreateModel) -> dict:
    return {
        "title": book_data.title,
        "author": book_data.author,
    }


@router.get("/get_headers")
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
