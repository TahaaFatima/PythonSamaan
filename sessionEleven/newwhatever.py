print("my name is {fname} and i'm {age} years old".format(fname="John",age=36))
print("my name is {fname} and i'm {age} years old".format(age=36,fname="John"))
print("my name is {0} and i'm {1} years old".format("John",36))
print("my name is {} and i'm {} years old".format("John",36))
txt = "The universe is {:,} years old"
print(txt.format(130000000000))
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
txt = "You scored {:.0%}"
print(txt.format(0.25))
txt = "we have {:<8} chickens"
print(txt.format(49))
