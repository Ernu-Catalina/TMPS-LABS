# Structural Design Patterns

**Author:** Ernu Catalina FAF-223

## Objectives
1. Study and understand the Structural Design Patterns.
2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
3. Implement some additional functionalities using structural design patterns.

## Used Structural Design Patterns
- **Composite Pattern**: This pattern is used to compose objects into tree-like structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.

- **Decorator Pattern**: This pattern is used to add new functionality to an object dynamically. It allows behavior to be added to an individual object without affecting the behavior of other objects from the same class.

- **Flyweight Pattern**: This pattern is used to reduce the number of objects created by sharing common objects. It helps in optimizing memory usage when multiple identical objects are created.

## Implementation

### Composite Pattern Implementation

**File: `composite_order.py`**
```python
class OrderBase:
    def get_price(self):
        return 0

    def get_info(self):
        return "No info available"


class BookItem(OrderBase):
    def __init__(self, book):
        self.book = book

    def get_price(self):
        return self.book.price

    def get_info(self):
        return self.book.get_info()


class BookBundle:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_price(self):
        return sum(item.get_price() for item in self.items)

    def get_info(self):
        return "Bundle:\n" + "\n".join(item.get_info() for item in self.items)
```
**Explanation:**  
The `OrderBase` class represents the basic interface with `get_price` and `get_info` methods. The `BookItem` class represents a single book item, while the `BookBundle` class groups multiple items together into a bundle. This design allows combining individual `BookItem` objects into larger structures like `BookBundle` while keeping a uniform interface for calculating prices and retrieving information.

### Decorator Pattern Implementation

**File: `decorator.py`**
```python
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
```
**Explanation:**  
The `Order` class serves as a base for the decorator classes. `Discount` and `GiftWrap` are decorators that modify the behavior of an existing order. `Discount` applies a discount to the price, while `GiftWrap` adds a gift wrap fee to the price. Both decorators extend the `Order` class, allowing them to be applied dynamically to orders.

### Flyweight Pattern Implementation

**File: `flyweight.py`**
```python
from book import Book

class BookFactory:
    def __init__(self):
        self.books = {}

    def get_book(self, title, author, price):
        key = (title, author)
        if key not in self.books:
            self.books[key] = Book(title, author, price)
        return self.books[key]
```
**Explanation:**  
The `BookFactory` is a Flyweight class that manages the creation of `Book` objects. It stores a cache of already created books and reuses existing ones if a book with the same title and author is requested. This optimizes memory usage, as books with the same attributes are shared rather than creating new instances.

## Execution

**File: `main.py`**
```python
from book import Book
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

print(bundle.get_info())
print("Bundle Price:", bundle.get_price())

discounted_bundle = Discount(bundle, 0.2)
wrapped_bundle = GiftWrap(discounted_bundle, gift_wrap_fee=2)

print("Discounted Bundle Price:", discounted_bundle.get_price())
print("Gift Wrapped Discounted Bundle Price:", wrapped_bundle.get_price())
```
**Explanation:**  
In `main.py`, the Flyweight pattern is used to create shared `Book` instances. The Composite pattern is used to create a book bundle, and the Decorator pattern is applied to the bundle to add discounts and gift wrap. This demonstrates how these patterns work together to manage the creation, modification, and pricing of a bookstore order.

## Conclusions
In this project, I implemented multiple structural design patterns in the context of a bookstore system. The **Composite Pattern** allowed me to manage both individual books and book bundles with a unified interface. The **Decorator Pattern** provided flexibility in applying additional features like discounts and gift wrapping to orders. Finally, the **Flyweight Pattern** optimized memory usage by reusing book instances with identical attributes. These design patterns helped make the system more modular, maintainable, and efficient, showcasing their effectiveness in real-world applications.