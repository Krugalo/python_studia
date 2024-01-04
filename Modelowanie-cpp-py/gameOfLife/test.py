plik = 'GameOfLife-075.txt'

try:
    f = open(plik, 'r')
    check = 1
except:
    print('error')

if check == 1:
    lines = f.readlines()
    f.close()

    lista = []
    for x in range(0, 11):
        lista.append(lines[x+80])

    lista2 = []
    for x in lista:
        lista2.append(float(x[4:10]))

    print(lista2)

    print((max(lista2)+min(lista2))*0.5)