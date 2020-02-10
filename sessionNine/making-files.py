f = open("demofile.txt", "w")
f.write('This is the content')
# f.close()

f = open("demofile.txt", "a")
f.write('This is the changed --- content')
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())