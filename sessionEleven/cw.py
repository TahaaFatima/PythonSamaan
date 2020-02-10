x = "without,hello,bag,world"
y = x.split(',')
y.sort()
p = (','.join(y)).upper()
f = p.split(',')
g = sorted(''.join(f))
# print(g)
pp =''.join(g)
for x in range(len(g)+1):
    if x % 2 != 0:
        g[x] = g[x].lower()
print(g)
print(''.join(g))