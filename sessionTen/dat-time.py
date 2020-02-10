import datetime

x= datetime.datetime.now()
y= datetime.datetime(2018,6,1)
print(x.strftime("%B"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x)

print(datetime.datetime.now().timestamp())
t1 = datetime.date(year=2018, month=7, day=2)
t2 = datetime.date(year=2017, month=12, day=23)
t3 = t1 - t2
print("t3 = ", t3)