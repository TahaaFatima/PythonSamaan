class MyClass:
    x = [1, 2, 3]

class MyClass1:
    def __init__(self):
        self.x = [1, 2, 3]

obj  = MyClass() 
obj1 = MyClass()

obj.x[0] = 5
print(obj.x)
print(obj1.x)

obj2 = MyClass1()
obj3 = MyClass1()

obj2.x[0] = 5
print(obj2.x)
print(obj3.x)
