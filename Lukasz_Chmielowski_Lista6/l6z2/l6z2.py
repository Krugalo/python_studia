#Łukasz Chmielowski gr 1 zad 2 lista 6
import SzyfrCezara
a = int(input("Zaszyfrowac (1) czy odszyfrowac (2)? "))

if a == 1:
    zdanie = input("Podaj zdanie do zaszyfrowania: ")
    print(SzyfrCezara.cipher(zdanie))
elif b == 2:
    zdanie = input("Podaj zdanie do odszyfrowania: ")
    print(SzyfrCezara.decipher(zdanie))
else:
    print("Zly input!!!")
