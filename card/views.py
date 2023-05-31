from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from datetime import datetime
from .forms import *
import iyzipay
import json
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib import messages
import pprint
from django.core.exceptions import ObjectDoesNotExist
def index(request):
    cards = Card.objects.all()
    kategoris = ''
    kategoriler = Kategori.objects.all()
    if request.GET.get('kategoris'):
        kategoris = request.GET.get('kategoris')
        cards = Card.objects.filter(
            Q(isim__icontains = kategoris) |
            Q(kategori__isim__icontains = kategoris)
        )
    if request.method == 'POST':
        begen(request)
        return redirect('index')  

    context = {
        'cards': cards,
        'kategoris':kategoris,
        'kategoriler':kategoriler
    }
    
    return render(request, 'index.html',context)

api_key = 'sandbox-itoor2P6Y6NRCI9L3LXXhmN77dYhPCXD'
secret_key = 'sandbox-kIfE2XIYfPPLU9If0HQkMogJI9TTU5Sf'
base_url = 'sandbox-api.iyzipay.com'


options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}
sozlukToken = list()

def payment(request):
    context = dict()

    buyer={
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address={
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items=[
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]

    request={
        'locale': 'tr',
        'conversationId': '123456789',
        'price': '1',
        'paidPrice': '1500',
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://127.0.0.1:8000/result/",
        "enabledInstallments": ['2', '3', '6', '9'],
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        # 'debitCardAllowed': True
    }

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, options)

    #print(checkout_form_initialize.read().decode('utf-8'))
    page = checkout_form_initialize
    header = {'Content-Type': 'application/json'}
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)
    print(type(json_content))
    print(json_content["checkoutFormContent"])
    print("************************")
    print(json_content["token"])
    print("************************")
    sozlukToken.append(json_content["token"])
    return HttpResponse(json_content["checkoutFormContent"])


@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    context = dict()

    url = request.META.get('index')

    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': sozlukToken[0]
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)
    print("************************")
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print("************************")
    print(sozlukToken[0])   # Form oluşturulduğunda 
    print("************************")
    print("************************")
    sonuc = json.loads(result, object_pairs_hook=list)
    #print(sonuc[0][1])  # İşlem sonuç Durumu dönüyor
    #print(sonuc[5][1])   # Test ödeme tutarı
    print("************************")
    for i in sonuc:
        print(i)
    print("************************")
    print(sozlukToken)
    print("************************")
    if sonuc[0][1] == 'success':
        context['success'] = 'Başarılı İŞLEMLER'
        return HttpResponseRedirect(reverse('success'), context)

    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız'
        return HttpResponseRedirect(reverse('failure'), context)

    return HttpResponse(url)



def success(request):
    context = dict()
    context['success'] = 'İşlem Başarılı'

    messages.success(request, 'Ödeme Başarılı')
    return redirect('index')


def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'

    template = 'fail.html'
    return render(request, template, context)

def cardDetay(request, cardDetayId):
    cardDetay = Card.objects.get(id=cardDetayId)
    # if request.method == 'POST':
    #     if request.user.is_authenticated:
    #         cardDetayId = request.POST['cardDetayId']
    #         card = Card.objects.get(id = cardDetayId)
    #         girisDate = datetime.strptime(request.POST['girisDate'], '%Y-%m-%d').date()
    #         cikisDate = datetime.strptime(request.POST['cikisDate'], '%Y-%m-%d').date()
    #         fark = (cikisDate - girisDate).days
    #         if Rezerve.objects.filter(owner = request.user, card = card, odendiMi = False).exists():
    #             rezerv = Rezerve.objects.get(owner=request.user, card=card, odendiMi=False)
    #             rezerv.gun = fark
    #             rezerv.toplamFiyat = fark * rezerv.card.fiyat
    #             rezerv.save()
    #             messages.success(request, 'Rezerve edildi')
    #             return redirect('pay')
    #         else:
    #             rezerv = Rezerve.objects.create(owner=request.user, card=card, gun=fark, toplamFiyat=fark * card.fiyat)
    #             rezerv.save()
    #             messages.success(request, 'Rezerve edildi')
    #             return redirect('pay')
    #     else:
    #         messages.warning(request,'Lütfen giriş yapınız')
    #         return redirect('index')
    if 'comment' in request.POST:
        yorum = request.POST['yorum']
        yorums = Yorum.objects.create(
            isim=request.user,
            yorum=yorum,
            card=cardDetay
        )
        yorums.save()
        messages.success(request, 'Yorum yapıldı')
        return redirect('cardDetay', cardDetayId=cardDetayId)
    
    yorumlar = Yorum.objects.filter(card=cardDetay)
    
    if 'sil' in request.POST:
        yorumId = request.POST['userYorum']
        yorums = Yorum.objects.get(id=yorumId)
        yorums.delete()

    context = {
        'cardDetay': cardDetay,
        'yorumlar': yorumlar,
    }
    return render(request, 'cardDetay.html', context)


def create(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.isim = request.user
            card.save()
            return redirect('index')
    context = {
        'form': form
    }        
    return render(request, 'create.html',context)

def begen(request):
    if 'begen' in request.POST:    
        cardId = request.POST['cardId']
        card = Card.objects.get(id = cardId)
        if 'begen' in request.POST:
            if Card.objects.filter(like__in= [request.user] , id = cardId).exists():
                card.like.remove(request.user)
            
                card.save()
            else:
                card.like.add(request.user)
                card.save() 

def favori(request):
    begeni = Card.objects.filter(like__in = [request.user])
    uzunluk = len(begeni)
    print(uzunluk)
    if request.method == 'POST':
        begen(request)
        return redirect('favori')
    begen(request)
    context={
        'begeni' : begeni,
        'uzunluk' :uzunluk
    }
    return render(request, 'favori.html',context)

def rezerve(request):
    user = request.user
    rezervim = Rezerve.objects.filter(owner=user, odendiMi=False)
    toplam = 0
    for i in rezervim:
        toplam += i.toplamFiyat

    if request.method == 'POST':
        if 'pay' in request.POST:
            if Pay.objects.filter(owner = request.user, odendiMi = False).exists():
                return redirect('payment')
            else:
                pay = Pay.objects.create(
                    owner = request.user, 
                    toplamFiyat = toplam
                )
                pay.rezerve.add(*rezervim)
                pay.save()
                return redirect('payment')

    context = {
        'rezervim': rezervim,
        'toplam': toplam
    }
    return render(request, 'pay.html', context)

def profil(request):
    user = request.user
    posts = Card.objects.filter(evsahibi = user)
    context = {
        'posts':posts,
    }
    return render(request,'profil.html', context)

def hesap(request):
    profil = request.user
    
    context={
        'profil':profil
    }
    return render(request, 'hesap.html', context) 

def profilGuncelle(request):
    user = request.user.profil
    forms = HesapForm(instance=user)
    if request.method == 'POST':
        forms = HesapForm(request.POST,request.FILES,instance = user)
        if forms.is_valid():
            forms.save()
            messages.success(request,'Profil bilgileri güncellendi')
            return redirect('hesap')
    context = {
        'forms':forms
    }
    return render(request ,'profilGuncelle.html',context)
# İlan 

# İlan 
def ilan1(request):
    return render(request, 'ilan1.html')


def ilan2(request):
    return render(request,'ilan2.html')


def ilan11(request):
    return render(request, 'ilan11.html')

def pay(request):
    return render(request, 'pay.html')

def sartlar(request):
    return render(request, 'sartlar.html')
