class Item:
    pay_rate = 0.8  # Class attribute

    def __init__(self, name: str, price: float, quantity=0):   # Magic method
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("Phone", 1000, 1)
item1.apply_discount()
print(item1.price)




