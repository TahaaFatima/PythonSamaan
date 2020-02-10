""" a = ('b', 'g', 'h', 'f', 'a')
x = sorted(a)
print(x)

x = sorted(a, reverse = True)
print(x)
 """

""" def take_element(elem):
    return elem[0]

random = [(2,2), (3,4), (4,1), (1,3)]

sorted_list = sorted(random, key = take_element)

print('Sorted List: ', sorted_list) """

""" li = [(2, 15), (3, 5), (65, 5), (8, 5)]

li_sorted = sorted(li, key = lambda x:sum(x), reverse = True)
print(li_sorted)

li = [(2, 15), (3, 5), (65, 5), (8, 5)]

li_sorted = sorted(li, key = lambda elem:elem[0] + elem[1])
print(li_sorted) """

prod_list = [
    {
        'name'     : 'Doohickey',
        'price'    : 40,
        'weight'   : 10,
        'discount' : 0.15
    },
    {
        'name'     : 'Widget',
        'price'    : 50,
        'weight'   : 10,
        'discount' : 0.05
    },
    {
        'name'     : 'Doohickey',
        'price'    : 40,
        'weight'   : 8,
        'discount' : 0.15
    },
    {
        'name'     : 'Gadget',
        'price'    : 65,
        'weight'   : 7,
        'discount' : 0.2
    }
]

# print(sorted(prod_list, key = lambda p:p['price']))
result = sorted(prod_list, key = lambda p:p['weight'])
# print(result)
result = sorted(prod_list, key = lambda p:p['weight'])
print(sorted(result, key = lambda p:p['price'], reverse = True))
