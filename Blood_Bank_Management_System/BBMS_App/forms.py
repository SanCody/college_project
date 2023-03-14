from django import forms
from .models import Donor_Detail, Patient_Detail

class DonorForm(forms.ModelForm):
    class Meta:
        model= Donor_Detail
        fields= ["id", "name", "gender", "email", "contact", "address", "date", "blood", "volume"]
class patientForm(forms.ModelForm):
    class Meta:
        model= Patient_Detail
        fields= ["patientName", "patientAge", "patientGender", "patientContact", "patientBlood", "patientBloodVolume", "patientPhysician", "patientStatus", "patientRequestDate", "patientRequisitionDate"]
