key = {'A': 'N', 'B': 'O', 'C': 'A', 'D': 'T', 'E': 'R', 'F': 'B', 'G': 'E', 'H': 'C', 'I': 'F', 'J': 'X',
           'K': 'X', 'L': 'D', 'M': 'Q', 'N': 'G', 'O': 'Y', 'P': 'L', 'Q': 'K', 'R': 'H', 'S': 'V', 'T': 'I',
           'U': 'J', 'V': 'M', 'W': 'P', 'X': 'Z', 'Y': 'S', 'Z': 'W',
           'a': 'n', 'b': 'o', 'c': 'a', 'd': 't', 'e': 'r', 'f': 'b', 'g': 'e', 'h': 'c', 'i': 'f', 'j': 'x',
           'k': 'x', 'l': 'd', 'm': 'q', 'n': 'g', 'o': 'y', 'p': 'l', 'q': 'k', 'r': 'h', 's': 'v', 't': 'i',
           'u': 'j', 'v': 'm', 'w': 'p', 'x': 'z', 'y': 's', 'z': 'w'}

def Monoencrypt(plaintext):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                # print(key[char])
                cipher_char = key[char]
            else:
                # index = ord(char) - ord('a')
                cipher_char = key[char]
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext

def Monodecrypt(plaintext):
    reversed_key = { val:key for key, val in key.items() }
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                # print(key[char])
                cipher_char = reversed_key[char]
            else:
                # index = ord(char) - ord('a')
                cipher_char = reversed_key[char]
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext


