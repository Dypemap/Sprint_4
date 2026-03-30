import pytest

from main import BooksCollector


@pytest.mark.parametrize('name', ['Книга'])
def test_add_new_book_has_empty_genre(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert name in collector.books_genre
    assert collector.books_genre[name] == ''


@pytest.mark.parametrize(
    'invalid_name',
    [
        '',
        'а' * 41,
    ],
    ids=['empty', 'too_long'],
)
def test_add_new_book_invalid_name_not_added(invalid_name):
    collector = BooksCollector()
    collector.add_new_book(invalid_name)
    assert invalid_name not in collector.books_genre


def test_add_new_book_same_title_twice_after_genre_set():
    collector = BooksCollector()
    title = '1984'
    collector.add_new_book(title)
    collector.set_book_genre(title, 'Фантастика')
    collector.add_new_book(title)
    assert list(collector.books_genre.keys()).count(title) == 1
    assert collector.books_genre[title] == 'Фантастика'


def test_set_book_genre():
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
def test_set_book_genre_invalid_does_not_change(name, genre):
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.books_genre['Дюна'] = ''
    collector.set_book_genre(name, genre)
    assert collector.books_genre.get('Дюна') == ''


@pytest.mark.parametrize(
    'name, expected',
    [
        ('Есть', 'Комедии'),
        ('Нет', None),
    ],
    ids=['in_dictionary', 'missing'],
)
def test_get_book_genre(name, expected):
    collector = BooksCollector()
    collector.add_new_book('Есть')
    collector.set_book_genre('Есть', 'Комедии')
    assert collector.get_book_genre(name) == expected


def test_get_books_with_specific_genre():
    collector = BooksCollector()
    for t in ('А', 'Б', 'В'):
        collector.add_new_book(t)
    collector.set_book_genre('А', 'Детективы')
    collector.set_book_genre('Б', 'Мультфильмы')
    collector.set_book_genre('В', 'Мультфильмы')
    assert collector.get_books_with_specific_genre('Мультфильмы') == ['Б', 'В']


def test_get_books_genre_returns_current_state():
    collector = BooksCollector()
    collector.add_new_book('X')
    d = collector.get_books_genre()
    assert d == {'X': ''}
    collector.set_book_genre('X', 'Комедии')
    assert collector.get_books_genre()['X'] == 'Комедии'


@pytest.mark.parametrize(
    'genre, for_children',
    [
        ('Ужасы', False),
        ('Мультфильмы', True),
    ],
    ids=['age_restricted', 'kids_ok'],
)
def test_get_books_for_children_by_genre(genre, for_children):
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', genre)
    names = collector.get_books_for_children()
    assert 'Книга' in names if for_children else 'Книга' not in names


def test_add_book_in_favorites_and_no_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Звёздные войны')
    collector.add_book_in_favorites('Звёздные войны')
    collector.add_book_in_favorites('Звёздные войны')
    assert collector.get_list_of_favorites_books() == ['Звёздные войны']


def test_add_book_in_favorites_unknown_book_ignored():
    collector = BooksCollector()
    collector.add_book_in_favorites('Чужая')
    assert collector.get_list_of_favorites_books() == []


def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('М')
    collector.add_book_in_favorites('М')
    collector.delete_book_from_favorites('М')
    assert collector.get_list_of_favorites_books() == []


def test_get_list_of_favorites_books_returns_list():
    collector = BooksCollector()
    collector.add_new_book('Первая')
    collector.add_new_book('Вторая')
    collector.add_book_in_favorites('Первая')
    collector.add_book_in_favorites('Вторая')
    assert collector.get_list_of_favorites_books() == ['Первая', 'Вторая']
