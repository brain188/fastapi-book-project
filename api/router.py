from fastapi import APIRouter, HTTPException
from api.routes import books

router = APIRouter()

    
api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])


@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = books.db.get_book(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


