from django.forms import ModelForm
from .models import *

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['kategori','adress','ev_ozellikleri','aciklama','resim1','resim2','resim3','resim4','resim5','fiyat','girisDate','cikisDate']
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control w-50'}) 

class HesapForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['isim','soyisim','meslek','telefon','profilresim']
    def _init_(self,args,*kwargs):
        super(HesapForm,self)._init_(args,*kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control w-100 btn btn-primary'})   