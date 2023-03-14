from django.shortcuts import render, redirect, HttpResponse
from .models import Donor_Detail, Patient_Detail
from .forms import DonorForm, patientForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum

# Create your views here.


def blood_available(req):
    context = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    bloodVolume = Donor_Detail.objects.filter(blood=context).aggregate(Sum('volume'))
    
    print(bloodVolume)
    return render(req, "blood_available.html") # type: ignore


# <---------------|| Donations ||--------------->

def donations(req):
    # show table
    details = Donor_Detail.objects.all().values()
    donorTable = { 'details': details }

    # insert table
    donorForm = DonorForm(req.POST or None)
    print("oh yeah")
    if donorForm.is_valid():
        donorForm.save()
        print("success")
        messages.success(req, "New Donar Added")
    else:
        donorForm = DonorForm()
        print("failed")
    # view table
        
    return render(req, "donations.html", donorTable)

def viewDonor(req, id):
    viewData = Donor_Detail.objects.get(id = id)
    donorDetail = {'viewDonor': viewData}

    return render(req, "viewDonor.html", donorDetail)


def update_donor(req, id):
    update_data = Donor_Detail.objects.get(id = id)
    
    donor = {"donor": update_data}
    update_form = DonorForm(req.POST or None
    , instance=update_data)
    if update_form.is_valid():
        update_form.save()
        return redirect('/Donations')
    
    return render(req, "update_donorForm.html", donor )
    

def delete_donor(req, id):
    donor_data = Donor_Detail.objects.get(id = id)
    donor_data.delete()
    print("donor deleted")
    return redirect("/Donations")


# <---------------|| Requests ||--------------->

def requests(req):
    # show table
    patientDetails = Patient_Detail.objects.all().values()
    patientTable = { 'patientDetails': patientDetails }
    # insert table
    patient_form = patientForm(req.POST or None)
    print("oh yeah")
    if patient_form.is_valid():
        patient_form.save()
        print(" request success")
        messages.success(req, "New Donar Added")
    else:
        patient_form = patientForm(req.POST or None)
        print("request failed")
    return render(req, "requests.html", patientTable)

def viewPatient(req, id):
    viewData = Patient_Detail.objects.get(id = id)
    patientDetail = {'viewPatient': viewData}
    return render(req, "viewPatient.html", patientDetail)

def update_patient(req, id):
    update_data = Patient_Detail.objects.get(id = id)
    
    patient = {"patient": update_data}
    update_form = patientForm(req.POST or None
    , instance=update_data)
    if update_form.is_valid():
        update_form.save()
        return redirect('/Requests')
    
    return render(req, "updatePatient.html", patient )

def delete_patient(req, id):
    patient_data = Patient_Detail.objects.get(id = id)
    patient_data.delete()
    print("patient deleted")
    return redirect("/Requests")













def profile(req):
    print(timezone.now)
    return render(req, "profile.html")

# def logout(req):
#     return render(req, "")