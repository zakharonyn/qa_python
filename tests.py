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

    # 1. Проверяем, что можно добавить только уникальные книги, без повторов
    def test_add_new_book_add_two_identical_book_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')

        assert len(collector.get_books_rating()) == 1

    # 2. Проверяем, что книге присваевается именно тот рейтинг, который мы присваеваем
    def test_set_book_rating_8_show_rating_8(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)

        assert collector.books_rating['Преступление и наказание'] == 8

    # 3. Проверяем, что функция возвращает корректный рейтинг
    def test_get_book_rating_test_book_rating_5(self):
        collector = BooksCollector()

        collector.add_new_book('test book')
        collector.set_book_rating('test book', 5)

        assert collector.get_book_rating('test book') == 5

    # 4. Проверяем, что функция выводит список с книгами только с заданным рейтингом
    def test_get_books_with_specific_rating_rating_8_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)

        collector.add_new_book('Вокруг света за 80 дней')
        collector.set_book_rating('Вокруг света за 80 дней', 3)

        collector.add_new_book('Хоббит')
        collector.set_book_rating('Хоббит', 10)

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Мастер и Маргарита', 8)

        assert collector.get_books_with_specific_rating(8) == ['Преступление и наказание', 'Мастер и Маргарита']

    # 5. Проверяем, что функция возвращает словарь с ожидаемыми элементами
    def test_get_books_rating_two_books_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)

        collector.add_new_book('Вокруг света за 80 дней')
        collector.set_book_rating('Вокруг света за 80 дней', 3)

        assert collector.get_books_rating() == {'Преступление и наказание': 8, 'Вокруг света за 80 дней': 3}

    # 6. Проверяем, что книги добавляется в избранное
    def test_add_book_in_favorites_test_book_true(self):
        collector = BooksCollector()

        collector.add_new_book('test book')
        collector.add_new_book('python byte')


        collector.add_book_in_favorites('test book')
        collector.add_book_in_favorites('python byte')

        assert collector.favorites == ['test book', 'python byte']

    # 7. Проверяем, что книга удаляется из списка избранных
    def test_delete_book_from_favorites_test_book_1_book(self):
        collector = BooksCollector()

        collector.add_new_book('test book')
        collector.add_new_book('python byte')

        collector.add_book_in_favorites('test book')
        collector.add_book_in_favorites('python byte')

        collector.delete_book_from_favorites('test book')

        assert collector.favorites == ['python byte']

    # 8. Проверяем, что функция выводит список избранных книг
    def test_get_list_of_favorites_books_3_books_3_books(self):
        collector = BooksCollector()

        collector.add_new_book('test book')
        collector.add_new_book('python byte')
        collector.add_new_book('bear byte')

        collector.add_book_in_favorites('test book')
        collector.add_book_in_favorites('python byte')
        collector.add_book_in_favorites('bear byte')

        assert collector.get_list_of_favorites_books() == ['test book', 'python byte', 'bear byte']