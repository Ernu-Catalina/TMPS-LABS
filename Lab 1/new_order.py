class Order:
    def __init__(self):
        self.items = []
        self.customer = None

    def __str__(self):
        items_str = ', '.join(item.get_info() for item in self.items)
        return f"Order for {self.customer}: {items_str}"


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
