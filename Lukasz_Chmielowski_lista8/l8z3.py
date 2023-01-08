#£ukasz Chmielowski gr 1 zad 3 lista 8

#pesel ma 11 cyfr
#1-6 data urodzenia
#7-9 libcza porzadkowa
#10 plec
#11 cyfra kontrolna

import os
import random

destiny = input('Podaj lokacje zapisu pliku: ')
final = os.path.join(destiny, 'PESEL.txt')

try:  
    fWRITE = open(final,"w")
except:
    os.mkdir(destiny)
    fWRITE = open(final,"w")

ans = ''

for n in range(1,11):
    for x in range(1,12):
        a = random.randint(0,9)
        ans += str(a)
    fWRITE.write(ans + '\n')
    print(ans)
    ans = ''

fWRITE.close()
print('utworzono plik ' + final)




