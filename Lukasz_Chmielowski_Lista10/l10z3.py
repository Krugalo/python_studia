#£ukasz Chmielowski gr 1 zad 3 lista 10
class Elementy:
    
    def __init__(self, lis):
        self.lista = []
        for el in lis:
            self.lista.append(el)

    #def sortowanie(self):
        


listka = []
for el in range(0,100,1):
    listka.append(el)

a = Elementy(listka)
print(a.sortowanie())
#chunks = [data[x:x+100] for x in range(0, len(data), 100)]
