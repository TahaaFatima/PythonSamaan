class MyNumbers:
    def __init__(self):
        self.my_list = ['a', 'b', 'c']

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < 3:
            x = self.a
            self.a += 1
            return self.my_list[x]
        else:
            raise StopIteration

my_obj = MyNumbers()
my_iter = iter(my_obj)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))



""" for x in my_iter:
    print(x) """