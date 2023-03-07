from django import forms
from .models import Donor_Detail

class DonorForm(forms.ModelForm):
    class Meta:
        model= Donor_Detail
        fields= ["id", "name", "gender", "email", "contact", "address", "date", "blood", "volume"]
