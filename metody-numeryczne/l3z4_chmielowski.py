import numpy as np

#alorytm eliminacji Gaussa z wykorzystaniem lambdy
def gauss(a,b):
    #bierzemy rozmiar wektora, zeby wiedziec jak duze sa macierze
    n = len(b)

    #lecimy po kolumnach i wierszach
    for j in range(0, n-1):
        for i in range(j+1, n):
            if a[i,j] != 0.0:
                #liczymy lambde
                l = a[i,j]/a[j,j]
                #nowy rzad macierzy, dzialamy od razu na calym wierszu
                a[i, j+1:n] = a[i, j+1:n] - l*a[j, j+1:n]
                #nowy wektor
                b[i] = b[i] - l*b[j]
    #wstawiamy elementy do macierzy końcowej od końca
    for j in range(n-1, -1, -1):
        #mnozymy a i b, odejmujemy i dzielimy
        b[j] = (b[j] - np.dot(a[j, j+1:n], b[j+1:n]))/a[j,j]

    return b

#dajemy macierze i liczymy
a = np.array([[-1, 2, 3],[1, 2, 3],[-4, 0, 2]])
b = np.array([0, 1, 0.5])

print("A =\n", a, '\n')
print("B =\n", b, '\n')

x = gauss(a,b)

print("x =\n", x)



