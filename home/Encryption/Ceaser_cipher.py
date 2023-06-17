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
def Ceasor_Cipher_Encrypt(plainText, key):
    cipher_text = ""
    for char in plainText:
        if char.isalpha():
            if char.isupper():
                new_upper_alpha = {val[0]:key for key, val in Alpha_dict.items()}
                char_no = int(new_upper_alpha[char])
                cipher_char = str((char_no+key)%26)
                print(cipher_char)
                encrypted_char = Alpha_dict[cipher_char][0]

            else:
                new_lower_alpha = {val[1]:key for key, val in Alpha_dict.items()}
                char_no = int(new_lower_alpha[char])
                cipher_char = str((char_no+key)%26)
                encrypted_char = Alpha_dict[cipher_char][1]
                

            cipher_text += encrypted_char
        else:
            cipher_text += char
    
    return cipher_text


def Ceasor_Cipher_Decrypt(CipherText, key):
    plainText = ""
    for char in CipherText:
        if char.isalpha():
            if char.isupper():
                new_upper_alpha = {val[0]:key for key, val in Alpha_dict.items()}
                char_no = int(new_upper_alpha[char])
                cipher_char_no = (char_no-key)
                if cipher_char_no<0:
                    cipher_char_no += 26
                else:
                    cipher_char_no %= 26
                # print(cipher_char)
                decrypted_char = Alpha_dict[str(cipher_char_no)][0]

            else:
                new_lower_alpha = {val[1]:key for key, val in Alpha_dict.items()}
                char_no = int(new_lower_alpha[char])
                cipher_char_no = (char_no-key)
                if cipher_char_no<0:
                    cipher_char_no = cipher_char_no + 26
                else:
                    cipher_char_no = cipher_char_no % 26
                decrypted_char = Alpha_dict[str(cipher_char_no)][1]
                

            plainText += decrypted_char
        else:
            plainText += char
    
    return plainText


# key = 15
# plaintext = input("Enter plain text:  ")
# # print(Ceasor_Cipher_Encrypt(plaintext, key))
# print(Ceasor_Cipher_Decrypt(plaintext, key))

