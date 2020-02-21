class Product:
    def __init__(self, name):
        self.name    = name
        self.__price = 0
        self.__qty   = 0

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_qty(self):
        return self.__qty

    def set_qty(self,qty):
        self.__qty = qty

    def show(self):
        print(f'Name : {self.name}')
        print(f'Price : {self.__price}')
        print(f'Quantity : {self.__qty}')

obj = Product('Lays')
obj.set_price(45)
obj.set_qty(5)
obj.show()