from django import forms
from .models import Donor_Detail, Patient_Detail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

class DonorForm(forms.ModelForm):
    class Meta:
        model= Donor_Detail
        fields= ["id", "name", "gender", "email", "contact", "address", "date", "blood", "volume"]
class patientForm(forms.ModelForm):
    class Meta:
        model= Patient_Detail
        fields= ["patientName", "patientAge", "patientGender", "patientContact", "patientBlood", "patientBloodVolume", "patientPhysician", "patientStatus", "patientRequestDate", "patientRequisitionDate"]

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'type':'text',
            'class':'form-control',
            'placeholder':'Name',
            'maxlength': '30',
            'minlength': '6'
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name':'email',
            'type':'email',
            'class':'form-control',
            'placeholder':'email'
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'class':'form-control',
            'placeholder':'Password',
            'minlength': '8'
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'type':'password',
            'class':'form-control',
            'placeholder':'Confirm Password',
            'minlength': '8'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'Username'
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'Password',
        'id':'password'
        }
    ))

class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'Old Password'
        }
    ))
    
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'New Password',
        'id':'cPassword'
        }
    ))

    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class': 'form-control', 
        'placeholder': 'Confirm Password',
        }
    ))

class EditUser(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({
                'class':'form-control',
                'placeholder':'username',
                'value': self.instance.username
            })
            self.fields['email'].widget.attrs.update({
                'class':'form-control',
                'placeholder':'email',
                'value': self.instance.email
            })

    
        
        