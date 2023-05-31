from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('cardDetay/<int:cardDetayId>',cardDetay,name='cardDetay'),
    path('ilan1/',ilan1,name='ilan1'),
    path('ilan2/', ilan2, name='ilan2'),
    path('create/',create, name='create'),
    path('ilan11/',ilan11, name='ilan11'),
    path('favori/', favori , name='favori'),
     path('sartlar/', sartlar, name='sartlar'),
    path('odeme/', payment, name='payment'),
    path('result/', result, name='result'),
    path('success/',success , name='success'),
    path('fail/',fail, name='failure'),
    path('pay/',pay, name='pay'),
    path('hesap',hesap,name='hesap'),
    path('profil/',profil,name='profil'),
    path('profilGuncelle/',profilGuncelle,name='profilGuncelle'),
]
