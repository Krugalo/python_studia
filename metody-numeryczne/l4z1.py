from scipy import optimize

def f(x):
    return (2*x**4+24*x**3+61*x**2-16*x+1)
lista = []
for i in range(-100,100):
    lista.append(i)
    
dodatnie=[]
ujemne=[]

for a in lista:
    if f(a) > 0:
        dodatnie.append(a)
    elif f(a) < 0:
        ujemne.append(a)

print("Dodatnie:")
print(dodatnie)
print("Ujemne:")
print(ujemne)

print(optimize.ridder(f,-10,-6))
