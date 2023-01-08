#Łukasz Chmielowski gr 1 zad 1 lista 6

import trojkat

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

if (a+b)<=c or (a+c)<=b or (b+c)<=a:
    print('Podano zle boki!')
else:
    print("Obwod trojkata wynosi: ")
    print(trojkat.obwod(a,b,c))

    print("Pole trojkata wynosi: ")
    print(trojkat.pole(a,b,c))

    print(trojkat.check(a,b,c))

    print(trojkat.kat(a,b,c))
