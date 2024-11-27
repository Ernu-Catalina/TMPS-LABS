from composite_order import BookItem, BookBundle
from decorator import Discount, GiftWrap
from flyweight import BookFactory
from strategy import PriceStrategy, WeekendDiscountStrategy, HolidayMarkupStrategy
from observer import Customer, OrderNotifier

# Create books using Flyweight pattern
book_factory = BookFactory()

book1 = book_factory.get_book("1984", "George Orwell", 19.99)
book2 = book_factory.get_book("Brave New World", "Aldous Huxley", 18.99)
book3 = book_factory.get_book("To Kill a Mockingbird", "Harper Lee", 14.99)

# Create book items
item1 = BookItem(book1)
item2 = BookItem(book2)
item3 = BookItem(book3)

# Create a bundle and add items
bundle = BookBundle()
bundle.add_item(item1)
bundle.add_item(item2)
bundle.add_item(item3)

print("\nIterating through bundle items:")
for item in bundle:
    print(item.get_info())

strategies = [
    ("Regular Price", PriceStrategy()),
    ("Weekend Discount", WeekendDiscountStrategy()),
    ("Holiday Markup", HolidayMarkupStrategy()),
]

for description, strategy in strategies:
    price = strategy.calculate_price(bundle.get_price())
    print(f"{description}: {price}")

discounted_bundle = Discount(bundle, 0.2)
wrapped_bundle = GiftWrap(discounted_bundle, gift_wrap_fee=2)

print("\nDiscounted Bundle Price:", discounted_bundle.get_price())
print("Gift Wrapped Discounted Bundle Price:", wrapped_bundle.get_price())

notifier = OrderNotifier()
customer1 = Customer("Alice")
customer2 = Customer("Bob")
notifier.add_observer(customer1)
notifier.add_observer(customer2)

notifier.notify_observers("Your order has been shipped!")
notifier.notify_observers("New promotional discounts available!")
