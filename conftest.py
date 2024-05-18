import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Мечтают ли электроовцы')
    collector.add_new_book('Преступление и наказание')
    collector.add_new_book('Психо')
    collector.add_new_book('Зомби')
    collector.add_new_book('Король лев')
    collector.add_new_book('Шерлок Холмс')
    collector.add_new_book('Властелин колец')
    collector.add_new_book('Дживс и Вустер')
    collector.set_book_genre('Мечтают ли электроовцы', 'Фантастика')
    collector.set_book_genre('Психо', 'Ужасы')
    collector.set_book_genre('Зомби', 'Ужасы')
    collector.set_book_genre('Король лев', 'Мультфильмы')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    collector.set_book_genre('Властелин колец', 'Фантастика')
    collector.set_book_genre('Дживс и Вустер', 'Комедии')

    return collector