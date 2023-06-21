from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from home.Encryption.Ceaser_cipher import Ceasor_Cipher_Encrypt
from home.Encryption.Ceaser_cipher import Ceasor_Cipher_Decrypt

from home.Encryption.monoalphabetic_cipher import Monoencrypt
from home.Encryption.monoalphabetic_cipher import Monodecrypt

from home.Encryption.Vigenère_Cipher import VigenereEncrypt
from home.Encryption.Vigenère_Cipher import VigenereDecrypt

from .models import CipherText


def userSignUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        pass2 = request.POST.get('pass1')

        user = User.objects.create(
            email = email,
            username = username,
        )
        user.set_password(pass1)
        user.save()
        return JsonResponse({"message":"User Registration successfull! Please login get access"})
    
    return render(request, 'index.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(username = username, password = pass1)
        if user is not None:
            login(request, user)
            return JsonResponse({"message":"Login successfull"})
        else:
            return JsonResponse({"message":"Invalid Credentials", "lable":"warning"})
        
    return render(request, 'index.html')
    

        
def EncryptText(request):
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
            alert = "Do you want to save your cipher text in database for use in future? "
        elif lable == "0":
            if algo_id == "1":
                outputText = Ceasor_Cipher_Decrypt(CipherText=inputText, key=int(key))
            elif algo_id == "2":
                outputText = Monodecrypt(plaintext=inputText)
            elif algo_id == "3":
                outputText = VigenereDecrypt(plainText=inputText, inputKey=key)
        else:
            return HttpResponse("Invalid request!")
       
        if algo_id == '2':
            key = 0
        context = {
            'outputText':outputText,
            'alert':alert,
            'cipherKey': key,
            'algo_id':algo_id,
        }
        return render(request, 'encrypt.html', context)
    return render(request, 'encrypt.html')

def index(request):
    return render(request, 'index.html')

def savedCipher(request):
    if request.method == 'POST':
        currentUser = request.user
        title = request.POST.get('title')
        Ciphertext = request.POST.get('CipherText')
        algo_id = request.POST.get('algo_id')
        cipherKey = request.POST.get('key')

        CipherObj = CipherText.objects.create(
            user = currentUser,
            title = title,
            text = Ciphertext,
            key = cipherKey,
            algo_id = algo_id
        )
        CipherObj.save()
        return JsonResponse({"message":"Cipher text saved successfully!"})
    return render(request, 'savedCipher.html')


def UserSavedCiphers(request):
    return render(request, 'savedCipher.html')