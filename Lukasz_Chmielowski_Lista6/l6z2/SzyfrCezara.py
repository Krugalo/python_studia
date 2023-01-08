#a -> 97
#z -> 122
#A -> 65
#Z -> 90
#ord('a') chr(97)

def cipher(zdanie):
    ans = ''
    lista = []
    
    for letter in zdanie:
        lista.append(letter)
        
    for litera in lista:
        temp = ord(litera)
        
        if 65 <= temp <= 90:
            pozycja = 26 - (91 - temp)
            zamiana = temp + pozycja
            if zamiana > 90:
                temp2 = zamiana - 90
                zamiana = 65 + temp2
            el = chr(zamiana)
            ans += el
            
        elif 97 <= temp <= 122:
            pozycja = 26 - (123 - temp)
            zamiana = temp + pozycja
            if zamiana > 122:
                temp2 = zamiana - 122
                zamiana = 97 + temp2
            el = chr(zamiana)
            ans += el
            
        else:
            ans += litera
    
    return ans

def decipher(zdanie):
    ans = ''
    lista = []
    
    for letter in zdanie:
        lista.append(letter)
        
    for litera in lista:
        temp = ord(litera)
        
       #work in progres
            
    return ans

print(cipher('abcdz ABCDZ'))
print(decipher('acegz ACGZ'))
