import math
import pygame
import os
import numpy as np

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
                F += r * i.m * j.m / pow(R,3)
                #print(R)
        if i.rigid == 1:
            i.v += F / i.m * dt
            i.x += i.v * dt
                
R = 1
Rx = [0, R]
Ry = [0, 0]
m = [1, 1]
counter = 0
path2 = 'owce2-d1d2.txt'

try:
    f2 = open(path2, 'w')
except:
    print('error 2')
    SystemExit

for v in np.arange(0.15, 1, 0.05):
    p = [planeta(pygame.math.Vector2(Rx[0],Ry[0]), #x,y
            pygame.math.Vector2(0,-v),  #u, v
            m[0],                       #m
            1),                         #rigid
        planeta(pygame.math.Vector2(Rx[1],Ry[1]), 
            pygame.math.Vector2(0, v),
            m[1],
            1)]

    t = 10
    dt = 0.00001
    tempT = 0

    #path = 'owce2-py-000001-v' + str(counter) + '.txt'
    counter += 1

    #try:
    #   f = open(path, 'w')
    #except:
    #    print('error 1')
    #    SystemExit

    x1min = 100
    x1max = -100
    y1min = 100
    y1max = -100

    while tempT < t :
        update(p, dt)

        if p[0].x[0] < x1min: #x1 min
            x1min = p[0].x[0]
        if p[0].x[0] > x1max: #x1 max
            x1max = p[0].x[0]
        if p[0].x[1] < y1min: #y1 min
            y1min = p[0].x[1]
        if p[0].x[1] > y1max: #y1 max
            y1max = p[0].x[1]

        #ans = str(p[0].x[0]) + " " + str(p[0].x[1]) + " " + str(p[1].x[0]) + " " + str(p[1].x[1]) + '\n'
        #f.write(ans)
        tempT += dt
    
    d1 = x1max - x1min
    d2 = y1max - y1min

    print(v)
    ans2 = str(v) + " " + str(d1/d2) + '\n'
    print(ans2)
    f2.write(ans2)

