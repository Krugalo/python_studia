#Łukasz Chmielowski gr 1 zad 1 lista 7
import time


N = int(input("Podaj ilosc szeregu Fibonacciego: "))

def iteracja(n):
    print("ITERACJA START")
    start = time.perf_counter()
    n1 = 0
    n2 = 1
    count = 0
    if n==1:
        print(n1)
    else:
        while count < N:
            print(n1)
            n3 = n1+n2
            n1 = n2
            n2 = n3
            count+=1
    end = time.perf_counter()
    print("ITERACJA KONIEC")
    print(end - start)

def rekurencja(n):
    if n in {0, 1}:
        return n
    temp = rekurencja(n - 1) + rekurencja(n - 2)
    return temp

iteracja(N)

print("REKURENCJA START")
start = time.perf_counter()
for n in range(N):
    print(rekurencja(n))
end = time.perf_counter()
print("REKURENCJA KONIEC")
print(end - start)
