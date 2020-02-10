def my_function():
    print('whatever')

def ek_aur_function():
    print(f'sum = {2 + 2}')

def name_print_karado(naam = 'default name', age = 1):
    print(f'Hello, {naam}')
    print(f'your age :  {age}')

def multiply(num,):
    return 5 * num

def add_num(num_one, num_two):
    return(f'{float(num_one) + float(num_two)}')

g_var = 'global var'

def this_func():
    l_var = 'local_var'
    print(g_var)
    print(l_var)


my_function()
ek_aur_function()
name_print_karado('Ye Naam',32)
name_print_karado('Ye Naam')
name_print_karado()
print(multiply(multiply(5)))
print(add_num(2.995,5.456))
this_func()
# print(l_var)