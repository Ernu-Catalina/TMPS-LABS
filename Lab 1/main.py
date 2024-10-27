from book import Book
from new_book import NewBook
from new_order import NewOrder

original_book = Book("Alice in Wonderland", "Lewis Carol", 29.99)
book_copy = original_book.copy()
book_copy.price = 24.99
print("Original Book:", original_book.get_info())
print("Copied Book:", book_copy.get_info())


new_book = NewBook.create_book("The Great Gatsby", "F. Scott Fitzgerald", 34.99)
print("New Book:", new_book.get_info())

order = (NewOrder()
         .set_customer("Jane Doe")
         .add_item(original_book)
         .add_item(new_book)
         .build())
print(order)
