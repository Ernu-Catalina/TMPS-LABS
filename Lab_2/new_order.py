from order import Order


class NewOrder:
    def __init__(self):
        self.order = Order()

    def set_customer(self, customer_name):
        self.order.customer = customer_name
        return self

    def add_item(self, book):
        self.order.items.append(book)
        return self

    def build(self):
        return self.order
