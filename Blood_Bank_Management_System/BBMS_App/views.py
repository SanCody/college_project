from django.shortcuts import render
from BBMS_App.models import Donar_Detail
from .forms import DonarForm
from django.contrib import messages
# Create your views here.
def blood_available(req):
    
    return render(req, "blood_available.html")

def donations(req):
    details = Donar_Detail.objects.all()
    return render(req, "donations.html", {'donar':details})

def insert_donation(req):
    if req.method =='POST':
        donarForm = DonarForm(req.POST)
        if donarForm.is_valid():
            donarForm.save()
            print("success")
            messages.success(req, "New Donar Added")
            return render(req, "donations.html")

        else:
            donarForm = DonarForm()
            return render(req, "donations.html")


def requests(req):
    return render(req, "requests.html")

def profile(req):
    return render(req, "profile.html")

# def logout(req):
#     return render(req, "")

