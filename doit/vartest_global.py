# vartet_global.py

from re import A


a = 1

def vartest():
    global a
    a = a + 1

vartest()

print(a)