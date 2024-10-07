### **Report: Implementing Two SOLID Principles in Python**

**Author**: Ernu Catalina FAF-223

### **Objectives:**
The goal of this lab is to implement two principles from the SOLID framework in a simple project. For this exercise, we will focus on the **Single Responsibility Principle (SRP)** and the **Open/Closed Principle (OCP)**. By doing so, we will gain practical experience in structuring classes that adhere to these principles and understand the benefits of doing so.

### **Implemented SOLID Principles**

#### **1. Single Responsibility Principle (SRP)**
The **Single Responsibility Principle (SRP)** says that a class should have only one responsibility, meaning it should have only one reason to change. A class that adheres to SRP should focus on a single task and delegate other concerns (such as logging, UI updates, etc.) to other classes.


For our example, we have two classes: one for managing the `User` data and another class for handling logging. The `User` class is only responsible for user-related tasks, and the `Logger` class manages the logging, adhering to SRP.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        # Save user to the database
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

**Explanation**:
- The `User` class is responsible solely for user-related tasks, such as saving the user.
- The `Logger` class is responsible for logging messages.

This separation follows SRP and keeps the classes focused on a single task.

---

#### **2. Open/Closed Principle (OCP)**
The **Open/Closed Principle (OCP)** states that software entities (such as classes, modules, and functions) should be **open for extension but closed for modification**. This means that we should be able to add new functionality without changing the existing code.

The `Discount` class is closed for modification, but open for extension. We can extend the discount system by adding new discount strategies through separate classes.

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

**Explanation**:
- The `Discount` class now takes a **strategy** object for applying discounts, which means the logic for each discount type is handled by different classes (e.g., `PercentageDiscount`, `FixedDiscount`).
- We can add new discount types by creating new strategy classes, without modifying the existing `Discount` class, thus following the OCP.

---

### **Conclusion**
In this project, we applied two of the five SOLID principles:

1. **Single Responsibility Principle (SRP)**: We refactored the `User` class by separating the logging functionality into a different class, ensuring that each class had only one responsibility.
2. **Open/Closed Principle (OCP)**: We refactored the `Discount` class so that new discount types could be added via extension (new strategy classes) without modifying the existing class, ensuring compliance with OCP.

By adhering to these principles, our code becomes more maintainable, easier to extend, and less prone to errors, especially when scaling up or adding new features.