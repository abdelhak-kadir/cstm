from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import order ,order_europ ,carte

class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']


class OrderForm(ModelForm):
    class Meta:
        model = order
    
        fields = ['name', 'prenom', 'cni', 'email', 'phone_number', 'type_colis', 'weight', 'from_colis', 'to_colis']


class europForm(ModelForm):
    class Meta:
        model = order_europ
        contry = forms.ChoiceField(choices=order_europ.contry_choices)
        fields = ['name', 'prenom', 'cni', 'email','contry', 'phone_number', 'type_colis', 'weight', 'from_colis', 'to_colis']
       

class CarteForm(forms.ModelForm):
    class Meta:
        model = carte
        fields = ['prenom','nom','cni','type_carte', 'formation_carte', 'permis', 'visite_medicale', 'phone', 'ville']

