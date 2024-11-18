class BookFacade:
    def __init__(self, book):
        self.book = book

    def get_book_details(self):
        return {
            "title": self.book.title,
            "author": self.book.author,
            "price": self.book.price
        }
