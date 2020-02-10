import os
import tempfile

print('gettempdir():',tempfile.gettempdir())
print('gettempprefix():',tempfile.gettempprefix())

tfp = tempfile.TemporaryFile(mode='w+t')
tfp.write('This is some data')
tfp.seek(0)
print(tfp.read())
print(tfp.name)
koisa_variable = input('Press any key : ')