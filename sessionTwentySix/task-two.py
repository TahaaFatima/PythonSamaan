user_input = int(input('Enter the ending integral : '))

this_dict = {}

for x in range(1,user_input+1):
    this_dict[x] = x**2

print(this_dict)