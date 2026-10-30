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
        # словарь books_rating, который нам возвращает метод get_books_rating(данный метод отсутствует в коде, поэтому заменен на get_books_genre), имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_set_genre_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
        assert collector.books_genre["Гордость и предубеждение и зомби"] == "Ужасы"

    def test_get_book_genre_name_book_return_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        assert collector.get_book_genre("Шерлок Хомс") == "Детективы"

    def test_get_books_with_specific_genre__detectives_returns_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.add_new_book('Десять негритят')
        collector.add_new_book('Простоквашино')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        collector.set_book_genre("Десять негритят", "Детективы")
        collector.set_book_genre("Простоквашино", "Мультфильмы")
        assert collector.get_books_with_specific_genre("Детективы") == ['Шерлок Хомс', 'Десять негритят']

    def test_get_books_for_children_filters_by_allowed_genres_list(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.add_new_book('Простоквашино')
        collector.add_new_book('Путешествие Алисы')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        collector.set_book_genre("Простоквашино", "Мультфильмы")
        collector.set_book_genre("Путешествие Алисы", "Фантастика")
        assert collector.get_books_for_children() == ["Простоквашино", "Путешествие Алисы"]

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        collector.add_book_in_favorites("Шерлок Хомс")
        assert collector.get_list_of_favorites_books() == ["Шерлок Хомс"]

    def test_add_book_in_favorites_repeated_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        collector.add_book_in_favorites("Шерлок Хомс")
        collector.add_book_in_favorites("Шерлок Хомс")
        assert collector.get_list_of_favorites_books() == ["Шерлок Хомс"]
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.set_book_genre("Шерлок Хомс", "Детективы")
        collector.add_book_in_favorites("Шерлок Хомс")
        collector.delete_book_from_favorites("Шерлок Хомс")
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Хомс')
        collector.add_new_book('Путешествие Алисы')
        collector.add_book_in_favorites("Шерлок Хомс")
        collector.add_book_in_favorites("Путешествие Алисы")
        assert collector.get_list_of_favorites_books() == ['Шерлок Хомс', 'Путешествие Алисы']




