class Vehicle():
    def __init__(self, price):
        self.price = price
        self.type = "unknown"
        self.color = "Black"
        self.company = "Unknown"

    def get_type(self):
        return self.type

    def __repr__(self):
        return repr((self.type, self.price, self.discount_price(), self.color))

    def discount_price(self):
        return self.price - (self.price * 0)


class Bike(Vehicle):
    def __init__(self, price):
        super().__init__(price)
        self.type = "Bike"

    def discount_price(self):
        return self.price - (self.price * 0.25)


class Car(Vehicle):
    def __init__(self, price):
        super().__init__(price)
        self.type = "Car"
        self.color = "White"


    def discount_price(self):
        return self.price - (self.price * 0.5)
