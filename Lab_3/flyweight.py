from book import Book


class BookFactory:
    def __init__(self):
        self.books = {}

    def get_book(self, title, author, price):
        key = (title, author)
        if key not in self.books:
            self.books[key] = Book(title, author, price)
        return self.books[key]
