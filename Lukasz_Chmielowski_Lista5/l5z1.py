#Łukasz Chmielowski gr 1 zad 1 lista 5

print("UWAGA! Program nie czyta polskich znakow!")

slowo = input("Podaj slownie liczbe od 1 do 59: ")

def jednosci(x):

    a = 0

    if "jeden" in x:
        a = 1
    elif "dwa" in x:
        a = 2
    elif "trzy" in x:
        a = 3
    elif "cztery" in x:
        a = 4
    elif "piec" in x:
        a = 5
    elif "szesc" in x:
        a = 6
    elif "siedem" in x:
        a = 7
    elif "osiem" in x:
        a = 8
    elif "dziewiec" in x:
        a = 9
    else:
        return a    
    return a

    

def nastki(x):

    a = 0

    if "jedenascie" in x:
        a = 11
    elif "dwanascie" in x:
        a = 12
    elif "trzynascie" in x:
        a = 13
    elif "czternascie" in x:
        a = 14
    elif "pietnascie" in x:
        a = 15
    elif "szesnascie" in x:
        a = 16
    elif "siedemnascie" in x:
        a = 17
    elif "osiemnascie" in x:
        a = 18
    elif "dziewietnascie" in x:
        a = 19
    else:
        return a
    return a


def dziesiatki(x):    
    a = 0

    if "dziesiec" in x:
        a = 10
    elif "dwadziescia" in x:
        a = 20
    elif "trzydziesci" in x:
        a = 30
    elif "czterdziesci" in x:
        a = 40
    elif "piecdziesiat" in x:
        a = 50
    else:
        return a
    return a



def zamiana(x):

    liczba = 0
    dziesiec = dziesiatki(x)
    nastka = nastki(x)
    jednostka = jednosci(x)

    if dziesiec == 0 and nastka == 0 and jednostka == 0:
        print("Podano zly input!!!")
        return x
    elif nastka == 0:
	#zeby usunac powtorki jednosci w dziesiatkach
        if dziesiec != 0:
            jednostka = jednosci(x[8:])
        liczba = dziesiec + jednostka
    elif nastka != 0:
        liczba = nastka
    return liczba
    
print(zamiana(slowo))
