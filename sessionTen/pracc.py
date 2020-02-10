import os
import tempfile

with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp,"tempfile.txt")
    tfp = open(path,"w+t")
    tfp.write("This is a temp file in a temp dir")
    tfp.seek(0)
    print(tfp.name)
    print(tfp.read())
    x=input('Enter : ')