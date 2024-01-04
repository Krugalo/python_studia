import math
import pygame
import os

class planeta:

    def __init__(self, 
                 x:pygame.math.Vector2, 
                 v:pygame.math.Vector2,
                 m:float, 
                 rigid:bool):
        self.x = x #x,y
        self.v = v #u,v
        self.m = m #masa
        self.rigid = rigid #ruch

def update(p, dt):
    for i in p:
        F = pygame.math.Vector2(0,0)
        r = pygame.math.Vector2(0,0)
        for j in p:
            if i!=j:
                r = j.x - i.x
                R = r.length()
                F += r * i.m * j.m / R
                #print(R)
        if i.rigid == 1:
            i.v += F / i.m * dt
            i.x += i.v * dt
                
R = 1
m = [1, 1]
p = [planeta(pygame.math.Vector2(0,0), #x,y
            pygame.math.Vector2(0,0),  
            m[0],
            0),
    planeta(pygame.math.Vector2(R,0), 
            pygame.math.Vector2(0,math.sqrt(m[1] / R)),
            m[1],
            1)]

t = 10
dt = 0.00001
tempT = 0

path = 'owce-py-000001.txt'

try:
    f = open(path, 'w')
except:
    print('error 1')
    SystemExit

while tempT < t :
    update(p, dt)
    print(p[1].x)
    ans = str(p[1].x[0]) + " " + str(p[1].x[1]) + '\n'
    f.write(ans)
    tempT += dt

e = abs(R - p[0].x.length() - p[1].x.length())
print(e)
#1      0.5218391889609832
#0.1    0.029221133409945255
#0.01   0.0028944464012323756
#0.001  0.00028853280539098414
#0.0001 2.8843459238370173e-05
#0.00001 2.884246940615398e-06