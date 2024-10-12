### Implementation Report: Two SOLID Principles in Python

**Author**: Ernu Catalina FAF-223

### **Objectives:**
The aim of this lab is to implement two principles from the SOLID framework in a simple project. I focused on the **Single Responsibility Principle (SRP)** and the **Open/Closed Principle (OCP)** to get hands-on experience in structuring classes according to these principles and to demonstrate the benefits.

### **Implemented SOLID Principles**

#### **1. Single Responsibility Principle (SRP)**
The Single Responsibility Principle (SRP) says that a class should have only one reason to change. For example, a class should only handle one responsibility, while other responsibilities, like logging or UI updates, should be managed by other classes.

In my project, I used two classes: one for handling user data and another for managing logs. The `User` class focuses only on user-related tasks, while the `Logger` class is responsible for logging.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        print(f"Saving user: {self.name}, {self.age}")

class Logger:
    @staticmethod
    def log(message):
        print(f"Log: {message}")

# Usage
user = User("John Doe", 30)
user.save()

# Log the action separately
Logger.log(f"{user.name} was saved to the database.")
```


The `User` class is responsible only for saving the user, while logging is delegated to the `Logger` class. This ensures that each class handles a single task, following SRP.

---

#### **2. Open/Closed Principle (OCP)**
The Open/Closed Principle (OCP) states that software should be open for extension but closed for modification. This means we can add new functionality without changing existing code.

In this case, I didn’t need to modify the `Discount` class to introduce new discount types. Instead, I created new strategies in separate classes.

```python
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
```

The `Discount` class now takes a strategy object for applying different types of discounts. I can add new discount strategies without changing the `Discount` class itself, which follows OCP.

---

### **Conclusion**
In this project, I applied two SOLID principles:

- **SRP (Single Responsibility Principle):** I separated the `User` and `Logger` classes so that each one handles only one responsibility.
- **Open/Closed Principle (OCP):** I refactored the `Discount` class to allow new discount strategies to be added without modifying the original class.

By following these principles, my code is easier to maintain, extend, and scale while minimizing the risk of introducing bugs when adding new features.