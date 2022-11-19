#Łukasz Chmielowski gr 1 zad 4 lista 5

klucz = {"a":"y", "e":"i", "i":"o", "o":"a", "y":"e"}
klucz2 = {"y":"a", "i":"e", "o":"i", "a":"o", "e":"y"}

x = int(input("Dla szyfrowania podaj 1, dla odszyfrowania podaj 2: "))
    
print("Podaj zdanie do zmiany:")
a = input()

def konwerter(zdanie):
    wynik = ""
    i = 0

    while i < len(zdanie):
        if zdanie[i] in klucz.keys():
            wynik += klucz[zdanie[i]]
        else:
            wynik += zdanie[i]
        i += 1

    return wynik

def decipher(zdanie):
    wynik = ""
    i = 0

    while i < len(zdanie):
        if zdanie[i] in klucz2.keys():
            wynik += klucz2[zdanie[i]]
        else:
            wynik += zdanie[i]
        i += 1

    return wynik

if x == 1:
    print("Zaszyfrowano:")
    print(konwerter(a))
elif x == 2:
    print("Odszyfrowano:")
    print(decipher(a))
else:
    print("Zly input!")


    
