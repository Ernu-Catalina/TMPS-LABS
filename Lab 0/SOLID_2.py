#Open/Closed Principle (OCP)
class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, discount_strategy):
        return discount_strategy.calculate_discount(self.price)


class PercentageDiscount:
    def calculate_discount(self, price):
        return price * 0.9  # 10% off


class FixedDiscount:
    def calculate_discount(self, price):
        return price - 10  # $10 off


# Usage
price = 100
discount = Discount(price)

percentage_discount = PercentageDiscount()
fixed_discount = FixedDiscount()

print(f"Price after percentage discount: {discount.apply_discount(percentage_discount)}")
print(f"Price after fixed discount: {discount.apply_discount(fixed_discount)}")