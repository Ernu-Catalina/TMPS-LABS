from book import Book


class NewBook:
    @staticmethod
    def create_book(title, author, price):
        return Book(title, author, price)
