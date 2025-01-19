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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
