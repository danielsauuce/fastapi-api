from fastapi import FastAPI, Body, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "publisher_date": "1925-04-10",
        "page_count": 180,
        "language": "English",
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "publisher_date": "1949-06-08",
        "page_count": 328,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Things Fall Apart",
        "author": "Chinua Achebe",
        "publisher": "William Heinemann",
        "publisher_date": "1958-06-17",
        "page_count": 209,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "publisher": "Bloomsbury",
        "publisher_date": "1997-06-26",
        "page_count": 223,
        "language": "English",
    },
    {
        "id": 5,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "publisher": "HarperCollins",
        "publisher_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publisher_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    publisher_date: str | None = None
    page_count: int | None = None
    language: str | None = None


@app.get("/books", response_model=list[Book])
async def get_books():
    return books


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book):
    new_book = book_data.model_dump()

    books.append(new_book)

    return new_book


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:

    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["publisher_date"] = book_update_data.publisher_date
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:

    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {"message": "Book deleted successfully", "book": book}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
