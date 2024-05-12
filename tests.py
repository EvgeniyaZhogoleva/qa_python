from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Роман')
        result = collector.get_book_genre('Преступление и наказание')
        assert result == 'Роман'

    @pytest.fixture
    def collector():
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фэнтези')
        return collector

    def test_get_book_genre(collector):
        result = collector.get_book_genre('Властелин колец')
        assert result == 'Фэнтези'

    def test_get_book_genre_non_existent_book(collector):
        result = collector.get_book_genre('Гарри Поттер')
        assert result is None

    @pytest.fixture
    def collector():
        collector = BooksCollector()
        collector.add_new_book('Самые страшные ужасы')
        collector.set_book_genre('Самые страшные ужасы', 'Ужасы')
        collector.add_new_book('Дневник зомби')
        collector.set_book_genre('Дневник зомби', 'Ужасы')
        collector.add_new_book('Очень страшные дела')
        collector.set_book_genre('Очень страшные дела', 'Ужасы')
        return collector
    def test_get_books_with_specific_genre(collector):
        result = collector.get_books_with_specific_genre('Ужасы')


    @pytest.fixture
    def collector():
        collector = BooksCollector()
        collector.add_new_book('Белоснежка')
        collector.set_book_genre('Белоснежка', 'Мультфильмы')
        collector.add_new_book('Король лев')
        collector.set_book_genre('Король лев', 'Мультфильмы')
        collector.add_new_book('Очень страшные дела')
        collector.set_book_genre('Бемби', 'Мультфильмы')
        return collector
    def test_get_books_for_children(collector):
        result = collector.get_books_for_children('Мультфильмы')
        assert result == ['Белоснежка', 'Король лев', 'Бемби']

    def test_get_books_not_for_children(collector):
        result = collector.book.genre('Ужасы')
        assert result is None

    #или так правильно?

    def test_get_books_for_children(collector):
        children_books = collector.get_books_for_children()
        for book in children_books:
            assert book.genre == 'Мультфильмы'
            assert book.genre != 'Ужасы'

    def test_add_and_get_favorites(self):
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        result = collector.get_list_of_favorites_books('Шерлок Холмс')
        assert result == 'Шерлок Холмс'

    def test_delete_book_from_favorites(self):
        collector.add_new_book('Жизнь Пи')
        collector.add_book_in_favorites('Жизнь Пи')
        collector.delete_book_from_favorites('Жизнь Пи')
        result = collector.get_list_of_favorites_books('Шерлок Холмс')
        assert result is None



