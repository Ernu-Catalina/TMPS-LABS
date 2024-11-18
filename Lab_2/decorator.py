class Order:
    def __init__(self, order):
        self.order = order

    def get_price(self):
        return self.order.get_price()

    def get_info(self):
        return self.order.get_info()


class Discount(Order):
    def __init__(self, order, discount):
        super().__init__(order)
        self.discount = discount

    def get_price(self):
        return self.order.get_price() * (1 - self.discount)


class GiftWrap(Order):
    def get_info(self):
        return f"{self.order.get_info()} (Gift Wrapped)"
