import pytest

from main import BooksCollector


class TestAddNewBook:
    @pytest.mark.parametrize('book_title', ['Книга', 'Война и мир'])
    def test_add_new_book_has_empty_genre(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        assert book_title in collector.books_genre
        assert collector.books_genre[book_title] == ''

    @pytest.mark.parametrize(
        'invalid_name',
        [
            '',
            'а' * 41,
        ],
        ids=['empty', 'too_long'],
    )
    def test_add_new_book_invalid_name_not_added(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.books_genre

    def test_add_new_book_same_title_only_once(self):
        collector = BooksCollector()
        title = '1984'
        collector.add_new_book(title)
        collector.add_new_book(title)
        assert list(collector.books_genre.keys()).count(title) == 1
        assert collector.books_genre[title] == ''


class TestSetBookGenre:
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.books_genre['Дюна'] == 'Фантастика'

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Несуществующая', 'Фантастика'),
            ('Дюна', 'Роман'),
        ],
        ids=['book_missing', 'genre_not_in_list'],
    )
    def test_set_book_genre_invalid_does_not_change(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get('Дюна') == ''


class TestGetBookGenre:
    @pytest.mark.parametrize(
        'book_name, expected_genre',
        [
            ('Есть', 'Комедии'),
            ('Нет', None),
        ],
        ids=['in_dictionary', 'missing'],
    )
    def test_get_book_genre(self, book_name, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Есть')
        collector.set_book_genre('Есть', 'Комедии')
        assert collector.get_book_genre(book_name) == expected_genre


class TestGetBooksWithSpecificGenre:
    def test_returns_titles_with_given_genre(self):
        collector = BooksCollector()
        for title in ('А', 'Б', 'В'):
            collector.add_new_book(title)
        collector.set_book_genre('А', 'Детективы')
        collector.set_book_genre('Б', 'Мультфильмы')
        collector.set_book_genre('В', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Б', 'В']


class TestGetBooksGenre:
    def test_returns_dict_matching_books_and_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        books_by_title = collector.get_books_genre()
        assert books_by_title == {'Гарри Поттер': ''}
        collector.set_book_genre('Гарри Поттер', 'Комедии')
        assert collector.get_books_genre()['Гарри Поттер'] == 'Комедии'


class TestGetBooksForChildren:
    def test_excludes_age_restricted_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Книга' not in children_books

    def test_includes_safe_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert 'Книга' in children_books


class TestFavorites:
    def test_add_book_in_favorites_and_no_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Звёздные войны')
        collector.add_book_in_favorites('Звёздные войны')
        collector.add_book_in_favorites('Звёздные войны')
        assert collector.get_list_of_favorites_books() == ['Звёздные войны']

    def test_add_book_in_favorites_unknown_book_ignored(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Чужая')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('М')
        collector.add_book_in_favorites('М')
        collector.delete_book_from_favorites('М')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        collector.add_new_book('Первая')
        collector.add_new_book('Вторая')
        collector.add_book_in_favorites('Первая')
        collector.add_book_in_favorites('Вторая')
        assert collector.get_list_of_favorites_books() == ['Первая', 'Вторая']
