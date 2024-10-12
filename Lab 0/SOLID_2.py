#Open/Closed Principle (OCP)
class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, discount_strategy):
        return discount_strategy.calculate_discount(self.price)

class PercentageDiscount:
    def calculate_discount(self, price):
        return price * 0.9

class FixedDiscount:
    def calculate_discount(self, price):
        return price - 10

price = 100
discount = Discount(price)

print(discount.apply_discount(PercentageDiscount()))
print(discount.apply_discount(FixedDiscount()))
