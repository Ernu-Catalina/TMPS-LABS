class PriceStrategy:
    def calculate_price(self, base_price):
        return base_price


class WeekendDiscountStrategy(PriceStrategy):
    def calculate_price(self, base_price):
        return round(base_price * 0.8, 2)  # 20% discount on weekends


class HolidayMarkupStrategy(PriceStrategy):
    def calculate_price(self, base_price):
        return round(base_price * 1.15, 2)  # 15% markup on holidays
