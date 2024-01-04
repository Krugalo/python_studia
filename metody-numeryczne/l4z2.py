#xn+1 = xn - f(xn)/f'(xn)
#sqrt(a) = x
#a = x**2
#f(x) = x**2 - a
#f'(x) = 2x
#f(x)/f'(x) = 0.5*(x - a/x)
#xn+1 = 0.5 * (xn + a/xn)

def newton(liczba, root):
    for iter in range(10):
        if iter == 0:
            x = 1

        f = x**root - liczba
        g = root*(x**(root-1))
        x = x - (f/g)
    return x

print(newton(3,5))
print(newton(3,5)**5)
