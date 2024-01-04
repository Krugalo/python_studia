#£ukasz Chmielowski gr 1 zad 3 lista 9

from asyncio import AbstractEventLoopPolicy
import matplotlib.pyplot as plt
import numpy as np

v0 = float(input('Podaj predkosc poczatkowa: '))
alpha = float(input('Podaj kat rzutu: '))
g = 9.81

alpha = np.deg2rad(alpha)

x1 = []
y1 = []
vvy = []
vvx = []

#rownania ruchu
vy = v0*np.sin(alpha)
vx = v0*np.cos(alpha)

tw = vy/g #czas wznoszenia
tc = tw*2 #czas lotu
t = np.linspace(0, tc, 100)

#wysokosc
h = (vy**2)/(2*g)
#zasieg
s = vx*tc

#printy
print('Maksymalna wysokosc: ' + str(h))
print('Zasieg rzutu: ' + str(s))
print('Czas lotu: ' + str(tc))

#tor ruchu
for k in t:
    x = vx * k
    y = vy * k - 0.5*g*k**2
    yv = vy - g*k
    x1.append(x)
    y1.append(y)
    vvy.append(yv)
    vvx.append(vx)

#zeby nie zeszlo pod ziemie
p = [i for i, j in enumerate(y1) if j < 0]
for i in sorted(p, reverse = True):
    del x1[i]
    del y1[i]

#plots
fig, axs = plt.subplots(3)

axs[0].plot(x1,y1)
axs[0].set_title('Tor lotu')
axs[1].plot(x1,t)
axs[1].set_title('x(t)')
axs[2].plot(vvx,t)
axs[2].plot(vvy,t)
axs[2].set_title('vx(t) oraz vy(t)')
plt.show()
