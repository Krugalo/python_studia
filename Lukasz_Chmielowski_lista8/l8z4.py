#£ukasz Chmielowski gr 1 zad 4 lista 8
import os

path = input("Podaj sciezke do pliku do odczytu: ")
path_end = os.path.basename(path)

#slownik do sprawdzania roku i miesiaca
year = {
    '81':'styczen 18',
    '82':'luty 18',
    '83':'marzec 18',
    '84':'kwiecien 18',
    '85':'maj 18',
    '86':'czerwiec 18',
    '87':'lipiec 18',
    '88':'sierpien 18',
    '89':'wrzesien 18',
    '90':'pazdziernik 18',
    '91':'listopad 18',
    '92':'grudzien 18',
    '01':'styczen 19',
    '02':'luty 19',
    '03':'marzec 19',
    '04':'kwiecien 19',
    '05':'maj 19',
    '06':'czerwiec 19',
    '07':'lipiec 19',
    '08':'sierpien 19',
    '09':'wrzesien 19',
    '10':'pazdziernik 19',
    '11':'listopad 19',
    '12':'grudzien 19',
    '21':'styczen 20',
    '22':'luty 20',
    '23':'marzec 20',
    '24':'kwiecien 20',
    '25':'maj 20',
    '26':'czerwiec 20',
    '27':'lipiec 20',
    '28':'sierpien 20',
    '29':'wrzesien 20',
    '30':'pazdziernik 20',
    '31':'listopad 20',
    '32':'grudzien 20',
    '41':'styczen 21',
    '42':'luty 21',
    '43':'marzec 21',
    '44':'kwiecien 21',
    '45':'maj 21',
    '46':'czerwiec 21',
    '47':'lipiec 21',
    '48':'sierpien 21',
    '49':'wrzesien 21',
    '40':'pazdziernik 21',
    '51':'listopad 21',
    '52':'grudzien 21',
    '61':'styczen 22',
    '62':'luty 22',
    '63':'marzec 22',
    '64':'kwiecien 22',
    '65':'maj 22',
    '66':'czerwiec 22',
    '67':'lipiec 22',
    '68':'sierpien 22',
    '69':'wrzesien 22',
    '70':'pazdziernik 22',
    '71':'listopad 22',
    '72':'grudzien 22',}

#sprawdzenie poprawnosci
def pesel(x): #dajemy liste intow
    #bierzemy liczbe kontrolna
    kontrolna = x[10]
    #wyliczamy sume wraz z wagami liczb w peselu:
    q = x[0] + x[1]*3 + x[2]*7 + x[3]*9 + x[4] + x[5]*3 + x[6]*7\
       + x[7]*9 + x[8] + x[9]*3
    q %= 10
    p = 10-q
    #warunki poprawnosci pesela:
    if kontrolna == 0 and q == 0:
        return True
    elif kontrolna == p:
        return True
    else:
        return False

#wyczytanie informacji
def info(line):
    ans=''
    ans += line
    ans += ' - '
    ans += line[4:6] 
    ans += ' '
    ans += year[line[2:4]]
    ans += line[0:2] 
    ans += ' '
    if int(line[9])%2 == 0:
        ans+='kobieta'
    else:
        ans+='mezczyzna'
    print(ans)


lista = []
check = 0

if path_end == 'PESEL.txt':
    try:
        f = open(path, "r")
        check = 1
        #print(path_end)
    except:
       print('Plik nie istnieje!')
else:
    print('Zla nazwa pliku!')

if check == 1:
    for n in range(0,10): #dla kazdej linii
        line = f.readline() #zczytujemy linie
        for ele in line[:-1]:
            lista.append(int(ele)) # robimy z niej liste intow
        if pesel(lista): #sprawdzamy poprawnosc pesela
            info(line[:-1])
            line = ''
            lista = []
        else:
            print(line[:-1] + ' - pesel niepoprawny')
            line = ''
            lista = []

    f.close()
