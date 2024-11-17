class Order:
    def __init__(self):
        self.items = []
        self.customer = None

    def __str__(self):
        items_str = ', '.join(item.get_info() for item in self.items)
        return f"Order for {self.customer}: {items_str}"
