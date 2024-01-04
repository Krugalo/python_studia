import math
plik = 'GameOfLife-03-final-200.txt'

check = 0
symulacje = 100

try:
    f = open(plik, 'r')
    check = 1
except:
    print('error')

if check == 1:
    lines = f.readlines()
    f.close()

    lista_fin=[]
    for sym in range(0,symulacje):
        lista = []
        for x in lines[sym:(sym+1)*1000]:
            b = x[:-2]
            lista.append(float(b))
        
        
        suma = 0
        for x in lista:
            suma += x

        sredniaAr = suma/len(lista)
        lista_fin.append(sredniaAr)
    
    suma2 = 0
    for x in lista_fin:
        suma2+= x

    sredniaArFin = suma2/len(lista_fin)
    print(sredniaArFin)

    #10 -> 0.09907632997956148
    #100 -> 0.05001512237592209
    #200 -> 0.044173859725289776
    #500 -> 0.04034439605454117
    #1000 -> 0.03890538685216672

    
    



