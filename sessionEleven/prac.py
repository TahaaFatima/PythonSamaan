txt = "For only {price: .2f} dollars!"
print(txt.format(price=49))

txt = "Hello, Whoever"
print(txt.swapcase())

txt = """For only {price:.3f} dollars!
whatever you say"""
print(txt.format(price=49))

txt ="This Is a Text"
print(txt.title())
txt ="This Is A Text"
x = txt.capitalize()
print(x)

print(id(txt))
print(id(x))