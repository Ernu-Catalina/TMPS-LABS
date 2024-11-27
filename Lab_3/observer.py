class Observer:
    def update(self, message):
        pass


class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Notification for {self.name}: {message}")


class OrderNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)
