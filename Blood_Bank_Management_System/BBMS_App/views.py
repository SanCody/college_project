from django.shortcuts import render
from .models import Donor_Detail
from .forms import DonorForm
from django.contrib import messages
# Create your views here.
def blood_available(req):
    
    return render(req, "blood_available.html")

def donations(req):
    details = Donor_Detail.objects.all().values()
    donorTable = { 'details': details }
    donorForm = DonorForm(req.POST or None)
    print("oh yeah")
    if donorForm.is_valid():
        donorForm.save()
        print("success")
        messages.success(req, "New Donar Added")
    else:
        print("failed")

    return render(req, "donations.html", donorTable)

def requests(req):
    return render(req, "requests.html")

def profile(req):
    return render(req, "profile.html")

# def logout(req):
#     return render(req, "")

