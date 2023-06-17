from django.shortcuts import render
from django.http import HttpResponse
from home.Encryption.Ceaser_cipher import Ceasor_Cipher_Encrypt
from home.Encryption.Ceaser_cipher import Ceasor_Cipher_Decrypt

from home.Encryption.monoalphabetic_cipher import Monoencrypt
from home.Encryption.monoalphabetic_cipher import Monodecrypt

from home.Encryption.Vigenère_Cipher import VigenereEncrypt
from home.Encryption.Vigenère_Cipher import VigenereDecrypt





# Create your views here.
def index(request):
    if request.method == 'POST':
        inputText = request.POST.get('inputText')
        algo_id = request.POST.get('algo_id')
        key = request.POST.get('key')
        lable = request.POST.get('lable')
        outputText = ""
        alert = ""
        if lable == "1":
            if algo_id == "1":
                outputText = Ceasor_Cipher_Encrypt(plainText=inputText, key=int(key))
            elif algo_id == "2":
                outputText = Monoencrypt(plaintext=inputText)
            elif algo_id == "3":
                outputText = VigenereEncrypt(plainText=inputText, inputKey=key)
            alert = "Your Cipher text also stored in your database for use in future!"
        elif lable == "0":
            if algo_id == "1":
                outputText = Ceasor_Cipher_Decrypt(CipherText=inputText, key=int(key))
            elif algo_id == "2":
                outputText = Monodecrypt(plaintext=inputText)
            elif algo_id == "3":
                outputText = VigenereDecrypt(plainText=inputText, inputKey=key)
        else:
            return HttpResponse("Invalid request!")
       
        context = {
            'outputText':outputText,
            'alert':alert,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
