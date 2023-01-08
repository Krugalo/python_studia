#£ukasz Chmielowski gr 1 zad 1 lista 8
import Cezar
import time
import os

#input
path = input("Podaj sciezke do pliku do odczytu: ")
destiny = input("Podaj sciezke do pliku docelowego: ")
shift = int(input("Podaj przesuniecie w szyfrowaniu: "))

if shift >= 1 and shift <= 10:

    #nazwa z czasem
    timestr = time.strftime("%Y%m%d")
    nazwa = 'plik_zaszyfrowany' + str(shift) + '_' + timestr + '.txt'

    #containers
    lista = []
    zdanie=''
    lista2=[]

    #otwieramy
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
            lista.append(ele)
        for ele in lista:
            zdanie +=  ele

        ans = Cezar.cipher(zdanie, shift)

        #z str do pliku
        for ele in ans:
            lista2.append(ele)
        for ele in lista2:
            fWRITE.write(ele)
    
        fWRITE.close()
        fOPEN = open(final,'r')

        #print(lista)
        #print(fOPEN.read())

        f.close()
        fOPEN.close()
        print('Utworzono plik o nazwie: ' + nazwa)
    except:
        print("Nie ma takiego pliku!!!")
else:
    print("Przesuniecie musi byc w zakresie 1-10!!!")



