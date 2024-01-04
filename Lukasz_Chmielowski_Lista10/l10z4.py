#£ukasz Chmielowski gr 1 zad 4 lista 10
#ListA.xml

import xml.etree.ElementTree as ET

class Przeliczanie:

    """Baza danych do przeliczania walut. Nalezy podac plik .xml ze strony 
    https://www.nbp.pl/home.aspx?f=/kursy/instrukcja_pobierania_kursow_walut.html
    
    .waluty - daje spis dostepnych walut
    .kody - daje spis kodow walut
    .przeliczniki - daje spis przelniczkow walut
    .kursy - daje kursy walut"""

    def __new__(cls, *args):
        if str in list(map(type,args)):
            return object.__new__(cls)
        else:
            return print('Bledne dane')

    waluty = []
    kody = []
    przeliczniki = [] #jednostka waluty, niektore maja 100 zamiast 1
    kursy = [] #wartosc jednostki waluty

    def __init__(self, path):

        #czytamy plik .xml i go mapujemy
        tree = ET.parse(path)
        root = tree.getroot()

        #zapelniamy listy potrzebnymi danymi

        for i in range(2,len(root)):
            self.waluty.append(root[i][0].text)

        for i in range(2,len(root)):
            self.przeliczniki.append(root[i][1].text.replace(',','.'))

        for i in range(2,len(root)):
            self.kody.append(root[i][2].text)

        for i in range(2,len(root)):
            self.kursy.append(root[i][3].text.replace(',','.'))

    def konwPLNto(self, liczbaPLN, kodWaluty):
        """Zwraca wartosc podanych PLN w podanej walucie"""
        pozycja = [i for i,x in enumerate(self.kody) if x == kodWaluty]
        return liczbaPLN * float(self.kursy[pozycja[0]]) * float(self.przeliczniki[pozycja[0]])

    def konwPLNfrom(self, liczbaWaluty, kodWaluty):
        """Zwraca wartosc PLN podana w innej walucie"""
        pozycja = [i for i,x in enumerate(self.kody) if x == kodWaluty]
        return liczbaWaluty / (float(self.kursy[pozycja[0]]) * float(self.przeliczniki[pozycja[0]]))

    def konwElse(self, liczbaWaluty1, kodWaluty1, kodWaluty2):
        """Zwraca wartosc drugiej waluty podanej w pierwszej walucie"""
        pozycja1 = [i for i,x in enumerate(self.kody) if x == kodWaluty1]
        pozycja2 = [i for i,x in enumerate(self.kody) if x == kodWaluty2]
        temp = liczbaWaluty1 * float(self.kursy[pozycja1[0]]) * float(self.przeliczniki[pozycja1[0]])
        return temp / (float(self.kursy[pozycja2[0]]) * float(self.przeliczniki[pozycja2[0]]))

test = Przeliczanie('LastA.xml')
print(test.waluty)
print(test.kody)
print(test.konwPLNto(10,'USD')) 
print(test.konwPLNfrom(43.52,'USD'))
print(test.konwElse(10,'USD','GBP'))