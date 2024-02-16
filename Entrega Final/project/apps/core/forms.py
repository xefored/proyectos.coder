from django import forms

from . import models

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User

class HotelesForm(forms.ModelForm):
    class Meta:
        model = models.Hoteles
        fields = "__all__"
        
class DestinosForm(forms.ModelForm):
    class Meta:
        model = models.Destinos
        fields = "__all__"



class CustonAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["usurname", "password"]
        widget={
            "usurname": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }