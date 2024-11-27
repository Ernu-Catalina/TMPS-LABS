class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_info(self):
        return f"Book: {self.title} by {self.author}, Price: {self.price}"
