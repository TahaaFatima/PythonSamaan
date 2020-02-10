set_one = {'a','b','c',1}
set_two = {1,2,3}
set_three = set_one.union(set_two)
print(set_three)

set_one.update(set_two)
print(set_one)