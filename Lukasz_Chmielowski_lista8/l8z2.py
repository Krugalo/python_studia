#£ukasz Chmielowski gr 1 zad 2 lista 8
import Cezar
import time
import os
import sys

#input
path = input("Podaj sciezke do pliku do odczytu: ")
destiny = input("Podaj sciezke do pliku docelowego: ")

path_end = os.path.basename(path)
file_name = os.path.splitext(path_end)[0]

#containers
zawartosc = []
zdanie = ''
zawartosc2 = []
lista = []

for ele in file_name:
    lista.append(ele)

if lista[18] == 0:
    shift = 10
elif lista[18] == '_':
    shift = int(lista[17])
else:
    sys.exit("Podano plik ze zlym formatem nazwy!")

#nazwa z czasem
timestr = time.strftime("%Y%m%d")
nazwa = 'plik_deszyfrowany' + str(shift) + '_' + timestr + '.txt'



try:
    f = open(path, "r")
    final = os.path.join(destiny, nazwa)

    try:  
        fWRITE = open(final,"w")
    except:
        os.mkdir(destiny)
        fWRITE = open(final,"w")

    #z pliku do str
    for ele in f.read():
        zawartosc.append(ele)
    for ele in zawartosc:
        zdanie +=  ele

    ans = Cezar.decipher(zdanie, shift)

    #z str do pliku
    for ele in ans:
        zawartosc2.append(ele)
    for ele in zawartosc2:
        fWRITE.write(ele)
   
    fWRITE.close()
    fOPEN = open(final,'r')

    f.close()
    fOPEN.close()
    print('Utworzono plik o nazwie: ' + nazwa)
except:
    print("Nie ma takiego pliku!!!")

