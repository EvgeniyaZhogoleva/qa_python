import pytest
from main import BooksCollector


def test_add_new_book_and_no_genre(collector):
    # тест на проверку, что книга добавилась и не имеет жанра
    collector.add_new_book('Незнайка на луне')
    assert collector.books_genre['Незнайка на луне'] == ''


def test_set_book_genre(collector):
    # тест на добавление жанра к существующей книге
    collector.set_book_genre('Преступление и наказание', 'Детективы')
    assert collector.get_book_genre('Преступление и наказание') == 'Детективы'


def test_get_book_genre(collector):
    # тест на получение жанра конкретной книги
    assert collector.get_book_genre('Мечтают ли электроовцы') == 'Фантастика'


def test_get_books_with_specific_genre(collector):
    # тест на выведение книг с определенным жанром
    assert collector.get_books_with_specific_genre('Ужасы') == ['Психо', 'Зомби']


def test_no_books_with_specific_genre(collector):
    # тест на случай, если нет книг определенного жанра
    assert collector.get_books_with_specific_genre('Романтика') == []


def test_get_books_for_children(collector):
    # тест что книга подходит детям
    children_books = collector.get_books_for_children()
    assert 'Король лев' in children_books


def test_get_books_not_for_children(collector):
    # тест что книга не подходит детям
    children_books = collector.get_books_for_children()
    assert 'Преступление и наказание' not in collector.get_books_for_children()


def test_add_book_in_favorites(collector):
    # тест на проверку, что книга добавляется в избранное
    collector.add_book_in_favorites('Шерлок Холмс')
    assert 'Шерлок Холмс' in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites(collector):
    # тест на проверку, что книга убирается из избранного
    collector.add_book_in_favorites('Властелин колец')
    collector.delete_book_from_favorites('Властелин колец')
    assert 'Властелин колец' not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books(collector):
    # тест на получение списка избранных книг
    collector.add_book_in_favorites('Дживс и Вустер')
    assert collector.get_list_of_favorites_books() == ['Дживс и Вустер']



