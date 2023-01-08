import math

def obwod(a,b,c):
    return (a+b+c)

def pole(a,b,c):
    p = obwod(a,b,c)/2
    pTroj = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return pTroj

def check(a,b,c):
    if a==b==c:
        return ("Trojkat rownoboczny")
    elif a==b!=c or a!=b==c or a==c!=b:
        return ("Trojkat rownoramienny")
    else:
        return ("Trojkat roznoboczny")

def kat(a,b,c):
    sinusAB = pole(a,b,c)*2/a/b
    sinusAC = pole(a,b,c)*2/a/c
    sinusCB = pole(a,b,c)*2/c/b
    if math.sin(math.pi/2) == sinusAB or\
       math.sin(math.pi/2) == sinusAC or\
       math.sin(math.pi/2) == sinusCB:
        return ("Trojkat prostokatny")
    elif math.sin(math.pi/2) > sinusAB and\
         math.sin(math.pi/2) > sinusAC and\
         math.sin(math.pi/2) > sinusCB:
        return ("Trojkat ostrokatny")
    elif math.sin(math.pi/2) < sinusAB or\
         math.sin(math.pi/2) < sinusAC or\
         math.sin(math.pi/2) < sinusCB:
        return ("Trojkat rozwartokatny")
    

