class Item:
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity


item1 = Item("Phone", 1000, 1)
item2 = Item("Laptop", 5000, 3)

print(item1.calculate_total_cost())
print(item2.calculate_total_cost())


