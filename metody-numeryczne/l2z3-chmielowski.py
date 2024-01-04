import math
def fun1(x):
    a = math.sqrt(x**2 + 1) - 1
    return a

def fun2(x):
    a = (x**2)/(math.sqrt(x**2 + 1) + 1)
    return a


for b in range(2, 30, 2):
    print(b, "\t", fun1(2**(-b)), "\t", fun2(2**(-b)))

#fun2 daje wiarygodniejsze wyniki
