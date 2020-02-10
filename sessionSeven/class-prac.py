this_set = {'apple','banana','cherry'}
this_set.add('orange')
this_set.update(['orange','mango','grapes'])
this_set.add('orange')
this_set.remove('banana')
this_set.discard('cherry')
this_set.discard('banana')

for x in this_set:
    print(x)

print('banana' in this_set)