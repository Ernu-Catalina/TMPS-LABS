# Structural Design Patterns

**Author:** Ernu Catalina FAF-223

## Objectives
1. Study and understand the Structural Design Patterns.
2. As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
3. Implement some additional functionalities using structural design patterns.

## Used Design Patterns
- **Prototype Pattern**: This pattern is used to create a new object by copying an existing object, which simplifies object creation when many similar objects are required.
  
- **Factory Method Pattern**: This pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created, promoting loose coupling.

- **Builder Pattern**: This pattern allows for step-by-step construction of a complex object, providing better control over the construction process and allowing for variations in the product being built.

## Implementation

### Prototype Pattern Implementation

**File: `book.py`**
```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_info(self):
        return f"{self.title} by {self.author}, Price: ${self.price}"

    def copy(self):
        return Book(self.title, self.author, self.price)
```
**Explanation:**  
The `Book` class represents a book in the bookstore. It includes attributes like title, author, and price. The `copy` method allows for creating a new instance of a book with the same attributes, implementing the Prototype pattern.

### Factory Method Pattern Implementation

**File: `new_book.py`**
```python
from book import Book


class NewBook:
    def create_book(title, author, price):
        return Book(title, author, price)
```
**Explanation:**  
The `NewBook` class has a static method called `create_book` that creates new `Book` objects. This method makes it easier to adjust the book creation process in the future if needed.
### Builder Pattern Implementation

**File: `new_order.py`**
```python
class Order:
    def __init__(self):
        self.items = []
        self.customer = None

    def __str__(self):
        items_str = ', '.join(item.get_info() for item in self.items)
        return f"Order for {self.customer}: {items_str}"


class NewOrder:
    def __init__(self):
        self.order = Order()

    def set_customer(self, customer_name):
        self.order.customer = customer_name
        return self

    def add_item(self, book):
        self.order.items.append(book)
        return self

    def build(self):
        return self.order
```
**Explanation:**  
The `Order` class represents a customer's order, including a list of books and the customer's name. The `NewOrder` class allows you to easily set the customer and add books to the order, and then returns the fully created `Order` object.

## Execution

**File: `main.py`**
```python
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
```
**Explanation:**  

The main file shows how all three design patterns are used. It clones a book with the Prototype pattern, creates a new book using the Factory Method, and builds an order with the Builder pattern. The output displays the details of the books and the completed order.

## Conclusions
In this project, I implemented three creational design patterns in the context of a bookstore domain. The Prototype pattern helps create a copy of book instances, the Factory Method simplifies the creation of new book objects, and the Builder pattern offers a structured way to build customer orders. These design patterns significantly improve the flexibility and maintainability of the code, demonstrating their effectiveness in real-world applications.