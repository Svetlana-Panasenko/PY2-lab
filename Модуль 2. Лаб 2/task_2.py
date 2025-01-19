BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


#  класс Book
class Book:
    def __init__(self, id_, name, pages):
        # атрибуты кники
        # идентификатор
        self.id = id_
        # название
        self.name = name
        # количество страниц
        self.pages = pages

    def __str__(self):
        # метод возвращает строковое представление книги
        return f'Книга "{self.name}"'

    def __repr__(self):
        # Метод возвращает строку, позволяющую создать точно такой же экземпляр класса
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


# класс Library
class Library:
    def __init__(self, books=None):
        # Инициализация библиотеки с списком книг
        if books is None:
            books = []  # Если аргумент не передан, создаем пустой список книг
        self.books = books  # Сохраняем список книг как атрибут экземпляра

    def get_next_book_id(self):
        # Метод возвращает идентификатор для добавления новой книги
        if not self.books:
            return 1  # Если библиотека пуста, возвращаем 1
        else:
            return self.books[-1].id + 1  # Иначе возвращаем id последней книги, увеличенный на 1

    def get_index_by_book_id(self, book_id):
        # Метод возвращает индекс книги в списке по id
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index  # Возвращаем индекс, если книга найдена
        raise ValueError("Книги с запрашиваемым id не существует")  # Вызываем ошибку, если книга не найдена


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
