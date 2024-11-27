from composite_order import BookItem, BookBundle
from decorator import Discount, GiftWrap
from flyweight import BookFactory

book_factory = BookFactory()

book1 = book_factory.get_book("1984", "George Orwell", 19.99)
book2 = book_factory.get_book("Brave New World", "Aldous Huxley", 18.99)
book3 = book_factory.get_book("To Kill a Mockingbird", "Harper Lee", 14.99)

item1 = BookItem(book1)
item2 = BookItem(book2)
item3 = BookItem(book3)

bundle = BookBundle()
bundle.add_item(item1)
bundle.add_item(item2)
bundle.add_item(item3)

for item in bundle:
    print(item.get_info())


print(bundle.get_info())
print("Bundle Price:", bundle.get_price())

discounted_bundle = Discount(bundle, 0.2)
wrapped_bundle = GiftWrap(discounted_bundle, gift_wrap_fee=2)

print("Discounted Bundle Price:", discounted_bundle.get_price())
print("Gift Wrapped Discounted Bundle Price:", wrapped_bundle.get_price())
