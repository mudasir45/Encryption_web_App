Alpha_dict = {
    '0': ('A', 'a'),
    '1': ('B', 'b'),
    '2': ('C', 'c'),
    '3': ('D', 'd'),
    '4': ('E', 'e'),
    '5': ('F', 'f'),
    '6': ('G', 'g'),
    '7': ('H', 'h'),
    '8': ('I', 'i'),
    '9': ('J', 'j'),
    '10': ('K', 'k'),
    '11': ('L', 'l'),
    '12': ('M', 'm'),
    '13': ('N', 'n'),
    '14': ('O', 'o'),
    '15': ('P', 'p'),
    '16': ('Q', 'q'),
    '17': ('R', 'r'),
    '18': ('S', 's'),
    '19': ('T', 't'),
    '20': ('U', 'u'),
    '21': ('V', 'v'),
    '22': ('W', 'w'),
    '23': ('X', 'x'),
    '24': ('Y', 'y'),
    '25': ('Z', 'z')
}

def VigenereEncrypt(plainText, inputKey):
    key = generateKey(inputKey, plainText)
    cipherText = ''
    j = 0
    for i in range(len(plainText)):
        char = plainText[i]
        if char.isalpha():
            keyChar = key[j]
            j += 1
            New_Lower_Alpha = {val[1]:key for key, val in Alpha_dict.items()}
            keyNo = int(New_Lower_Alpha[keyChar])
            if char.isupper():
                New_Upper_Alpha = {val[0]:key for key, val in Alpha_dict.items()}
                charNO = int(New_Upper_Alpha[char])
                cipherCharNo = str((charNO+keyNo)%26)
                cipherChar = Alpha_dict[cipherCharNo][0]
            else:
                charNO = int(New_Lower_Alpha[char])
                cipherCharNo = str((charNO+keyNo)%26)
                cipherChar = Alpha_dict[cipherCharNo][1]
            
            cipherText += cipherChar 
        else:
            cipherText += char
    return cipherText


def VigenereDecrypt(plainText, inputKey):
    key = generateKey(inputKey, plainText)
    cipherText = ''
    j = 0
    for i in range(len(plainText)):
        char = plainText[i]
        if char.isalpha():
            keyChar = key[j]
            j += 1
            New_Lower_Alpha = {val[1]:key for key, val in Alpha_dict.items()}
            keyNo = int(New_Lower_Alpha[keyChar])
            if char.isupper():
                New_Upper_Alpha = {val[0]:key for key, val in Alpha_dict.items()}
                charNO = int(New_Upper_Alpha[char])
                cipherCharNo = (charNO-keyNo)
                if cipherCharNo<0:
                    cipherCharNo += 26
                else:
                    cipherCharNo %= 26
                cipherChar = Alpha_dict[str(cipherCharNo)][0]
            else:
                charNO = int(New_Lower_Alpha[char])
                cipherCharNo = (charNO-keyNo)
                if cipherCharNo<0:
                    cipherCharNo += 26
                else:
                    cipherCharNo %= 26
                cipherChar = Alpha_dict[str(cipherCharNo)][1]
            
            cipherText += cipherChar 
        else:
            cipherText += char
    return cipherText


def generateKey(inputKey, plainText):
    lenth = len(inputKey)
    key = ""
    j = 0
    for i in range(len(plainText)):
        if plainText[i]!=' ':
            key += inputKey[j]
            j = (j+1)%lenth
    return key

 




