import pytest
from main import BooksCollector
from data import book_data

@pytest.fixture
def collector():
    collector = BooksCollector()
    for book, genre in book_data.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
    return collector