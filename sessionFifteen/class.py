class Test:
    def __init__(self):
        self.fname = 'My Name '

    def __repr__(self):
        return "self.fname"
    def __str__(self):
        return "member of Test"

my_obj = Test()
print(str(my_obj))