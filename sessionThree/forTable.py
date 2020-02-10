# for x in range(2,30,3):
#     print(x)

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# name = 'code girls'
# x = 0
# while x < 4:
#     print(x)
#     x += 1
# else:
#     print('Terminated')

table_of = float(input('Enter the number you want the table of : '))
limit    = 10
for x in range(1, limit+1):
    print(f'{table_of} x {x} = {table_of*x}')