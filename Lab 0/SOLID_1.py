#Single Responsibility Principle (SRP)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        # Save user to the database (placeholder)
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