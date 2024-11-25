class OrderBase:
    def get_price(self):
        return 0

    def get_info(self):
        return "No info available"


class BookItem(OrderBase):
    def __init__(self, book):
        self.book = book

    def get_price(self):
        return self.book.price

    def get_info(self):
        return self.book.get_info()


class BookBundle:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_price(self):
        return sum(item.get_price() for item in self.items)

    def get_info(self):
        return "Bundle:\n" + "\n".join(item.get_info() for item in self.items)
