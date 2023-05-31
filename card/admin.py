from django.contrib import admin
from .models import *
class RezerveAdmin(admin.ModelAdmin):
    list_display =('owner','card','gun','toplamFiyat','odendiMi')
    list_filter = ('owner','odendiMi')
# Register your models here.

admin.site.register(Card)
admin.site.register(Kategori)
admin.site.register(EvOzellik)
admin.site.register(Yorum)
admin.site.register(Rezerve, RezerveAdmin)
admin.site.register(Pay)
admin.site.register(Hesap)
admin.site.register(Profil)
