import random
""" for x in range(2):
    print(random.random())

print(random.randint(3,9))
print(random.uniform(3,9))
print(random.randrange(1,5))
print(random.randrange(1,6,2)) """

fruits=['apple','banana','cherry']
print(random.choice(fruits))                                                                                                                                                                       
print(random.choices(fruits,weights=[10,2,2],k=14))
print(random.sample(fruits,k=3))
random.shuffle(fruits)
print(fruits)
