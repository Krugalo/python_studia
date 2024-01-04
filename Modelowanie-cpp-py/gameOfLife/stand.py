import math

lista = [0.09907632997956148, 0.05001512237592209, 0.044173859725289776, 0.04034439605454117, 0.03890538685216672]

suma = 0
for x in lista:
    suma += x

srednia = suma/len(lista)
print(srednia)
# 0.054503018997496246

suma2 = 0
for x in lista:
    x -= srednia
    x = x*x
    suma2 += x

s = math.sqrt(suma2/len(lista)) #odchylenie
print(s)
# 0.022615771184915333

e = s/math.sqrt(len(lista))
print(e) #blad
# 0.01011408034661033