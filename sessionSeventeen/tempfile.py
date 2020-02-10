import tempfile


temp = tempfile.TemporaryFile(mode="w+")

try:
    temp.write('hello world')
    temp.seek(0)

    print(temp.read())
    print(temp.name)
    input('Enter any key')
finally:
    temp.close()

input("asdf")