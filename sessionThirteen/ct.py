# def num_generator(n):
#     num = 0
#     while num <= n:
#         if num % 7 == 0:
#             yield num
#             num += 1
#         else:
#             num += 1

# for i in num_generator(100):
#     print(i)

def num_gen(n):
    for x in range(n+1):
        if x % 7 != 0:
            yield x
        else:
            x += 1

for i in num_gen(100):
    print(i)