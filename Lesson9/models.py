from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str
    age: int
    favourite_book_id: int = None



class Book(BaseModel):
    id: int
    title: str
    author_id: int = None

class Author(BaseModel):
    id: int
    name: str




