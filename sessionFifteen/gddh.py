class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

elem = Element('my_name', 'some_symbol', 3)
print(elem)