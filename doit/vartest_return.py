# vartest_return.py

from re import A


a = 1

def vartest(a):
    a = a + 1
    return a

a = vartest(a)

print(a)