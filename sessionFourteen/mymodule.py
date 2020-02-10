class MyClass:

    def __init__(self):
        self.string_have = ''

    def setString(self):
        self.string_have = input('Enter the string : ')

    def getString(self):
        self.string_have = self.__upperString()
        print(self.string_have)

    def __upperString(self):
        return self.string_have.upper()