#Łukasz Chmielowski gr 1 zad 2 lista 9
import sys
from xml.sax import SAXReaderNotAvailable
import numpy as np

'''Wymagany format pliku zawiera kolejną daną w nowej lini, czyli tylko jedna liczba na linię'''

#containres
lista = []

suma = 0
srednia = 0
wariancja = 0
odchylenie = 0

#czytamy dane przekazane strumieniem
if len(sys.argv) < 2:
    linie = sys.stdin.readlines()
else:
    linie = []
    for el in sys.argv[1:]:
        linie.append(float(el))

for ele in linie:
    lista.append(float(ele))

#liczymy
for x in lista:
    suma += x

srednia = suma/len(lista)

for x in lista:
    wariancja += (x - srednia)**2

wariancja /= len(lista)
odchylenie = np.sqrt(wariancja)

#zwracamy
print('srednia wynosi: ' + str(srednia))
print('wariancja wynosi: ' + str(wariancja))
print('odchylenie wynosi: ' + str(odchylenie))
