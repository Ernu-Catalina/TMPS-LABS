#Single Responsibility Principle (SRP)
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

user = User("John Doe", 30)
user.save()
Logger.log(f"{user.name} was saved to the database.")