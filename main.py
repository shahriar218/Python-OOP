class Item:
    pay_rate = 0.8  # Class attribute: Added value after 20% discount

    def __init__(self, name: str, price: float, quantity=0):   # Magic method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7  # Added value after 30% discount
item2.apply_discount()
print(item2.price)
print(item2.calculate_total_cost())  # Printed price of three laptop on 30% discount






