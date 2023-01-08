def cipher(text, shift=1):
    ans = ''

    for i in range(len(text)):
        char = text[i]

        if char==' ':
            ans+=' '

        #duze litery
        elif (char.isupper()):
            ans += chr((ord(char) + shift-65) % 26 + 65)

        #male litery
        else:
            ans += chr((ord(char) + shift-97) % 26 + 97)

    return ans

#cipher(n) = decipher(26-n)
def decipher(text, shift=1):
    ans = ''

    letters = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:

        if char in letters:
            position = letters.find(char)
            new_pos = (position - shift) % 26
            new_char = letters[new_pos]
            ans += new_char
        else:
            ans+=char

    return ans
