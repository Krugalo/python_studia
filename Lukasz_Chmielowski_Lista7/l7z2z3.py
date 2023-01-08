#Łukasz Chmielowski gr 1 zad 2 i 3 lista 7
import random
import time

lista100 = []
lista200 = []
lista300 = []

kopia100 = []
kopia200 = []
kopia300 = []

n=20

for i in range(100):
    a = random.randint(0,n)
    lista100.append(a)
for i in range(200):
    a = random.randint(0,n)
    lista200.append(a)
for i in range(300):
    a = random.randint(0,n)
    lista300.append(a)

for i in lista100:
    kopia100.append(i)
for i in lista200:
    kopia200.append(i)
for i in lista300:
    kopia300.append(i)
##
def wstawianie(lista):
    start = time.perf_counter()
    
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j>=0 and lista[j]>temp:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = temp
        
    end = time.perf_counter()
    print("Czas wykonania wstawiania:")
    print(end-start)
##

##
def babelkowe(lista):
    start = time.perf_counter()
    
    dlugosc = len(lista)
    for i in range(dlugosc):
        for j in range(0, dlugosc - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    end = time.perf_counter()
    print("Czas wykonania bąbelkowania:")
    print(end-start)
##

print("Lista 100 elementów: ")
print(lista100)
wstawianie(lista100)
print(lista100)
babelkowe(kopia100)
print(kopia100)
print()
print("Lista 200 elementów: ")
print(lista200)
wstawianie(lista200)
print(lista200)
babelkowe(kopia200)
print(kopia200)
print()
print("Lista 300 elementów: ")
print(lista300)
wstawianie(lista300)
print(lista300)
babelkowe(kopia300)
print(kopia300)
