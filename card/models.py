import uuid
from django.db import models
import os
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='kategori_icons', blank=True, null=True) 

    def __str__(self):
        return self.isim
# Ev özellikleri
class EvOzellik(models.Model):
    isim =models.CharField(max_length=100)

    def __str__(self):
        return self.isim

# resimler eklendiğinde kendi dosya ismi olsun diye yapıldı
def custom_upload_to(instance, filename):
    # Resmin orijinal dosya adını alın
    original_filename, file_extension = os.path.splitext(filename)
    # Orijinal dosya adını kullanarak yeni bir dosya adı oluşturun
    new_filename = instance.kendi_eklediginiz_isim + file_extension
    # Yeni dosya adını ve "resimler/" klasörünü birleştirin
    return os.path.join('resimler/', new_filename)



class Card(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    isim = models.CharField(max_length=100)
    evsahibi = models.ForeignKey(User , on_delete= models.CASCADE , null=True, blank=True)
    adress = models.CharField(max_length=100, null=True)
    puan = models.IntegerField(default=0)
    girisDate = models.DateField()
    like = models.ManyToManyField(User , related_name="like", blank=True)
    cikisDate = models.DateField()
    aciklama = models.TextField(max_length=1000)
    fiyat = models.IntegerField()
    resim1 = models.FileField(upload_to='resimler/',null=True)
    resim2 = models.FileField(upload_to='resimler/',null=True)
    resim3 = models.FileField(upload_to='resimler/',null=True)
    resim4 = models.FileField(upload_to='resimler/',null=True)
    resim5 = models.FileField(upload_to='resimler/',null=True)
    ev_ozellikleri = models.ForeignKey(EvOzellik, on_delete=models.SET_NULL, null=True)
   

    def  __str__(self):
        return self.isim

class Yorum(models.Model):
    card = models.ForeignKey(Card, related_name='yorum', on_delete=models.CASCADE)
    yorum = models.TextField(max_length=200, verbose_name='Yorum')
    new_date = models.DateTimeField(auto_now_add=True)
    isim = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.isim.username
    
class Rezerve(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    gun = models.IntegerField()
    toplamFiyat = models.IntegerField()
    odendiMi = models.BooleanField(default=False)

    def __str__(self):
        return self.card.isim
    
class Pay(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rezerve = models.ManyToManyField(Rezerve)
    toplamFiyat = models.IntegerField()
    odendiMi = models.BooleanField(default=False)

    def __str__(self):
        return self.owner
    
class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='resimler/',null=True)

    def _str_(self):
        return self.user.username
    

class Profil(models.Model):
    id = models.UUIDField(primary_key=True , db_index= True , default=uuid.uuid4 , editable=False)
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    telefon = models.CharField(max_length=50)
    profilresim = models.FileField(upload_to='profilpic/' ,default='img/avatar.webp',blank=True)
    meslek = models.CharField(max_length=50)
    slug = models.SlugField(null=True , unique= True , db_index=True , blank=True , editable=False)

    def save(self, *args , **kwargs):
        self.slug = slugify(self.id)
        super().save(*args , **kwargs)

    def _str_(self):
        return str(self.isim)