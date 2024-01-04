import os

#czyszczenie ze smieci po bokach
def check(word):
    list = ['.',',',':',';','!','?','-','(',')','[',']','\"','\'','_','*']
    if len(word) >= 1:
        while True:
            try:
                if word[-1] in list:
                    word = word[:-1]
                elif word[1] in list:
                    word = word[1:]
                else:
                    return word
            except:
                #print(word + ' -> error')
                return word


#pliki
nazwa = 'zipf-py-dracula.txt'
path = 'dracula.txt'
#slownik na slowa
myDict = {}

#otwieramy zrodlo
try:
    f = open(path, 'r')
except:
    print('error 1')
    SystemExit

#zliczamy slowa
for line in f:
    for word in line.split():
        ans = check(str(word))
        try:
            myDict[ans] += 1
        except:
            myDict[ans] = 1

f.close()

#sortujemy od najwiekszej
sortedDict = sorted(myDict.items(), key=lambda x:x[1], reverse=True)
convDict = dict(sortedDict)
dictList = list(convDict.keys())

#otwiermy plik wynikowy
try:
    w = open(nazwa, 'w')
except:
    print('error 2')
    SystemExit

counter = 1
for ele in dictList:
    ans =str(counter) + " " + str(myDict[ele]) + "\t" +  str(ele) + '\n'
    w.write(ans)
    counter += 1

w.close()

