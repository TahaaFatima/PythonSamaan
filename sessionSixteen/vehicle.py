class Vehicle():
    def __init__(self, price):
        self.price    = price
        self.type     = "unknown"
        self.discount = 0
      
    def __repr__(self):
        return repr((self.type, self.price, self.discount))

    def get_type(self):
        return self.type

    def discount_price(self):
         return self.price - (self.discount * self.price)


    
class Bike(Vehicle):
  def __init__(self, price):
    super().__init__(price)
    self.type = "Bike"
    self.discount = 0.25


class Car(Vehicle):
  def __init__(self, price):
    super().__init__(price)
    self.type = "Car"
    self.discount = 0.5
