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
        return round(self.order.get_price() * (1 - self.discount), 2)


class GiftWrap(Order):
    def __init__(self, order, gift_wrap_fee=1):
        super().__init__(order)
        self.gift_wrap_fee = gift_wrap_fee

    def get_price(self):
        return self.order.get_price() + self.gift_wrap_fee

    def get_info(self):
        return f"{self.order.get_info()} (Gift Wrapped)"
