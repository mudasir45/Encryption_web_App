from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('EncryptText/', views.EncryptText, name="EncryptText"),
    path('user_login/', views.user_login, name="user_login"),
    path('userSignUp/', views.userSignUp, name="userSignUp"),
    path('savedCipher/', views.savedCipher, name="savedCipher"),
    path('UserSavedCiphers/', views.UserSavedCiphers, name="UserSavedCiphers"),
    path('EditSavedCipher/<int:id>/', views.EditSavedCipher, name="EditSavedCipher"),
]