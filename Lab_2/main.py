from composite_order import BookItem, BookBundle
from decorator import Discount, GiftWrap
from book import Book
from book_facade import BookFacade

book = Book("1984", "George Orwell", 19.99)

book_facade = BookFacade(book)
book_details = book_facade.get_book_details()

print(book_details)

book1 = Book("1984", "George Orwell", 15.99)
book2 = Book("Brave New World", "Aldous Huxley", 18.99)


item1 = BookItem(book1)
item2 = BookItem(book2)

bundle = BookBundle()
bundle.add_item(item1)
bundle.add_item(item2)

print("Total Price:", bundle.get_price())
print("Book Info:", bundle.get_info())

discounted_bundle = Discount(bundle, 0.1)
wrapped_bundle = GiftWrap(discounted_bundle)

print("Discounted Bundle Price:", wrapped_bundle.get_price())
print("Bundle Info:", wrapped_bundle.get_info())
