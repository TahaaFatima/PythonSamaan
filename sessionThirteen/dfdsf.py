# """ def generator_thr_iter():
#     yield 'xyz'
#     yield 246
#     yield 40.50

# """ value = generator_thr_iter()
# print(value) """

# """ for i in generator_thr_iter():
#     print(i)             """

# def num_generator(n):
#     num = 1
#     while True:
#         yield num
#         if num == n:
#             return
#         else:
#             num += 1

# for i in num_generator(10):
#     print(i*i) """

mytuple = ('apple','banana','pineapple')
myit    = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))