# BooksCollector — юнит-тесты

Проект для тренировки **pytest**: класс `BooksCollector` в `main.py`, тесты в `test.py`.

## Запуск тестов

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest test.py -v
```

## Реализованные тесты

Ниже перечислены тесты и то, что каждый из них проверяет. Часть сценариев объединена **параметризацией** (`@pytest.mark.parametrize`) — один и тот же код прогоняется с разными входными данными.

### `add_new_book`

| Тест | Описание |
|------|----------|
| `test_add_new_book_has_empty_genre` | После добавления корректного названия книга попадает в `books_genre`, жанр пустая строка. (Параметризовано по имени книги.) |
| `test_add_new_book_invalid_name_not_added` | Пустое имя и имя длиной 41 символ не добавляются в словарь. |
| `test_add_new_book_same_title_twice_after_genre_set` | Повторный вызов `add_new_book` для той же книги после `set_book_genre` не создаёт дубликат ключа; жанр не сбрасывается. |

### `set_book_genre`

| Тест | Описание |
|------|----------|
| `test_set_book_genre` | Для существующей книги и жанра из списка `genre` жанр сохраняется в `books_genre`. |
| `test_set_book_genre_invalid_does_not_change` | Жанр не меняется, если книги нет в словаре или жанр не из допустимого списка. (Два набора данных: «книга отсутствует», «жанр не из списка».) |

### `get_book_genre`

| Тест | Описание |
|------|----------|
| `test_get_book_genre` | Для книги в словаре возвращается установленный жанр; для отсутствующей книги — `None`. |

### `get_books_with_specific_genre`

| Тест | Описание |
|------|----------|
| `test_get_books_with_specific_genre` | Из нескольких книг с разными жанрами метод возвращает только те, у кого выбранный жанр (на примере «Мультфильмы»). |

### `get_books_genre`

| Тест | Описание |
|------|----------|
| `test_get_books_genre_returns_current_state` | Возвращаемый словарь соответствует текущему состоялению: сначала книга без жанра, после `set_book_genre` — с нужным жанром. |

### `get_books_for_children`

| Тест | Описание |
|------|----------|
| `test_get_books_for_children_by_genre` | Книга с жанром из `genre_age_rating` (например, «Ужасы») не попадает в список для детей; книга с «детским» жанром (например, «Мультфильмы») попадает. |

### `add_book_in_favorites` и `get_list_of_favorites_books`

| Тест | Описание |
|------|----------|
| `test_add_book_in_favorites_and_no_duplicate` | Книга из `books_genre` добавляется в избранное; повторный вызов не дублирует запись; список совпадает с `get_list_of_favorites_books`. |
| `test_add_book_in_favorites_unknown_book_ignored` | Книга, которой нет в `books_genre`, в избранное не попадает. |
| `test_get_list_of_favorites_books_returns_list` | Две добавленные в избранное книги возвращаются в ожидаемом порядке. |

### `delete_book_from_favorites`

| Тест | Описание |
|------|----------|
| `test_delete_book_from_favorites` | После удаления книга отсутствует в списке избранного. |

## Итог по прогонам pytest

Именованных тестовых функций: **13**. С учётом параметризации pytest выполняет **17** отдельных тестовых кейсов (видно в выводе `pytest -v`).
