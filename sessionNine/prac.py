import json
""" x = '{"name" : "John", "age" : 30, "country" : "Newyork"}'
print(type(x))
y=json.loads(x)
print(type(y))
print(y['age'])
x=json.dumps(y)
print(type(x)) """

print(json.dumps(['apple','banana']))
print(json.dumps(('apple','banana')))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))