""" class MyClass:
    x= 5
    y = [x for x in range(1,6)]

p1= MyClass()
print(MyClass.x)
print(p1.x)
print(p1.y) """

class Person:
    x = [1, 2, 3]
    def __init__(self,fname,age):
        self.name = fname
        self.__age  = age
        self.y    = [1, 2, 3]

    def show(self):
        print("Hello, I'm",self.name)
        print(f"I'm {self.__age} years old")
        # print(Person.x)

    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age

p = Person("John",36)
print(p.name)
# print(p.__age)
p.show()
p.set_age(45)
p.show()