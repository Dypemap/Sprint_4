# BooksCollector — юнит-тесты

Проект для тренировки **pytest**: класс `BooksCollector` в `main.py`, тесты в `test.py`.

## Запуск тестов

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest test.py -v
```

## Реализованные тесты

Тесты сгруппированы в **классы** (`TestAddNewBook`, `TestSetBookGenre`, …), внутри классов — методы `test_*`. Часть сценариев объединена **параметризацией** (`@pytest.mark.parametrize`).

### `add_new_book` — класс `TestAddNewBook`

| Метод | Описание |
|------|----------|
| `test_add_new_book_has_empty_genre` | Книга попадает в `books_genre` с пустым жанром. Параметризация по названию. |
| `test_add_new_book_invalid_name_not_added` | Пустое имя и имя длиной 41 символ не добавляются. |
| `test_add_new_book_same_title_only_once` | Повторный `add_new_book` с тем же названием не создаёт второй ключ; жанр остаётся пустым. |

### `set_book_genre` — класс `TestSetBookGenre`

| Метод | Описание |
|------|----------|
| `test_set_book_genre` | Для существующей книги и жанра из списка `genre` жанр сохраняется. |
| `test_set_book_genre_invalid_does_not_change` | Неизвестная книга или недопустимый жанр не меняют запись «Дюна» (после `add_new_book` пустой жанр уже по умолчанию). |

### `get_book_genre` — класс `TestGetBookGenre`

| Метод | Описание |
|------|----------|
| `test_get_book_genre` | Для книги в словаре — установленный жанр; для отсутствующей — `None`. |

### `get_books_with_specific_genre` — класс `TestGetBooksWithSpecificGenre`

| Метод | Описание |
|------|----------|
| `test_returns_titles_with_given_genre` | Среди книг с разными жанрами возвращаются только названия с выбранным жанром («Мультфильмы»). |

### `get_books_genre` — класс `TestGetBooksGenre`

| Метод | Описание |
|------|----------|
| `test_returns_dict_matching_books_and_genres` | Словарь отражает добавление книги и смену жанра; осмысленные имена переменных (`books_by_title`, понятное имя книги). |

### `get_books_for_children` — класс `TestGetBooksForChildren`

| Метод | Описание |
|------|----------|
| `test_excludes_age_restricted_genre` | Жанр с возрастным рейтингом («Ужасы») не попадает в список для детей. |
| `test_includes_safe_genre` | Безопасный жанр («Мультфильмы») попадает в список. Отдельные однозначные проверки без условий в `assert`. |

### `add_book_in_favorites`, `delete_book_from_favorites`, `get_list_of_favorites_books` — класс `TestFavorites`

| Метод | Описание |
|------|----------|
| `test_add_book_in_favorites_and_no_duplicate` | Добавление в избранное без дубля. |
| `test_add_book_in_favorites_unknown_book_ignored` | Книга не из `books_genre` не попадает в избранное. |
| `test_delete_book_from_favorites` | Удаление из избранного. |
| `test_get_list_of_favorites_books_returns_list` | Порядок нескольких избранных книг. |

## Итог по прогонам pytest

Именованных тестовых **методов** в классах: **14**. С учётом параметризации pytest выполняет **18** отдельных кейсов (см. `pytest -v`).
