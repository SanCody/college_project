from django import forms
from .models import Donar_Detail

class DonarForm(forms.ModelForm):
    class Meta:
        model= Donar_Detail
        fields= ["name", "gender", "email", "contact", "address", "date", "blood", "volume"]