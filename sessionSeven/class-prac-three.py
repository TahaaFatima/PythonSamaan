""" h_letters = [letter for letter in 'human']
print(h_letters)

this_list = []
for x in 'human':
    this_list.append(x)
print(this_list)

h_nums = [num*2 for num in range(1,11)]
print(h_nums)

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

number_list_two = ['Even' if x % 2 == 0 else 'Odd' for x in range(10)]
print(number_list_two) """

test_list = [('gfg', 1, True),('is', False),('best', 2)]
print(f'The original list : {test_list}')