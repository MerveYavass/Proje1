from django.shortcuts import render

def gizlilik(request):
    return render(request, 'gizlilik.html')

def siteharitasi(request):
    return render(request, 'siteharitasi.html')

def evtasima(request):
    return render(request, 'evtasima.html')

def cardDetay(request):
    return render(request, 'cardDetay.html')

def hesap(request):
    return render(request, 'hesap.html')

def harita(request):
    return render(request, 'harita.html')

def rezerve(request):
    return render(request, 'rezerve.html')

def seyahat(request):
    return render(request, 'seyahat.html')

def odeme(request):
    return render(request, 'odeme.html')

def mesajlar(request):
    return render(request, 'mesajlar.html')

def profil(request):
    return render(request, 'profil.html')