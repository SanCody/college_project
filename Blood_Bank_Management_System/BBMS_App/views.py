from django.shortcuts import render, redirect
from .models import Donor_Detail, Patient_Detail
from .forms import DonorForm, patientForm, RegistrationForm, LoginForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

# <---------------|| Home ||--------------->

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def blood_available(req):

    bloodVol ={
        "AP": float(str(eval(str(*Donor_Detail.objects.filter(blood='A+').aggregate(Sum('volume')).values())) or 0))*0.001, 

        "AN": float(str(eval(str(*Donor_Detail.objects.filter(blood='A-').aggregate(Sum('volume')).values())) or 0))*0.001,

        "BP": float(str(eval(str(*Donor_Detail.objects.filter(blood='B+').aggregate(Sum('volume')).values())) or 0))*0.001,
        
        "BN": float(str(eval(str(*Donor_Detail.objects.filter(blood='B-').aggregate(Sum('volume')).values())) or 0))*0.001,

        "ABP":float(str(eval(str(*Donor_Detail.objects.filter(blood='AB+').aggregate(Sum('volume')).values())) or 0))*0.001,  
        
        "ABN":float(str(eval(str(*Donor_Detail.objects.filter(blood='AB-').aggregate(Sum('volume')).values())) or 0))*0.001,

        "OP": float(str(eval(str(*Donor_Detail.objects.filter(blood='O+').aggregate(Sum('volume')).values())) or 0))*0.001,

        "ON": float(str(eval(str(*Donor_Detail.objects.filter(blood='O-').aggregate(Sum('volume')).values())) or 0))*0.001,    
    }

    return render(req, "blood_available.html", bloodVol) 

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def BloodAv(req, blood):
    bd = Donor_Detail.objects.filter(blood=blood)
    bloodD = { 'bd': bd }

    return render(req, "bloodDetail.html", bloodD)

# <---------------|| Donations ||--------------->

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
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

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def viewDonor(req, id):
    viewData = Donor_Detail.objects.get(id = id)
    donorDetail = {'viewDonor': viewData}

    return render(req, "viewDonor.html", donorDetail)


@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def update_donor(req, id):
    update_data = Donor_Detail.objects.get(id = id)
    
    donor = {"donor": update_data}
    update_form = DonorForm(req.POST or None
    , instance=update_data)
    if update_form.is_valid():
        update_form.save()
        return redirect('/Donations')
    
    return render(req, "update_donorForm.html", donor )

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def delete_donor(req, id):
    donor_data = Donor_Detail.objects.get(id = id)
    donor_data.delete()
    print("donor deleted")
    return redirect("/Donations")


# <---------------|| Requests ||--------------->

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
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

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def viewPatient(req, id):
    viewData = Patient_Detail.objects.get(id = id)
    patientDetail = {'viewPatient': viewData}
    return render(req, "viewPatient.html", patientDetail)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def update_patient(req, id):
    update_data = Patient_Detail.objects.get(id = id)
    
    patient = {"patient": update_data}
    update_form = patientForm(req.POST or None
    , instance=update_data)
    if update_form.is_valid():
        update_form.save()
        return redirect('/Requests')
    
    return render(req, "updatePatient.html", patient )

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def delete_patient(req, id):
    patient_data = Patient_Detail.objects.get(id = id)
    patient_data.delete()
    print("patient deleted")
    return redirect("/Requests")

# <---------------|| Signup ||--------------->

def signup(req):
    form = RegistrationForm() 
    if req.method == "POST":
        form = RegistrationForm(req.POST) 
        print("yes")
        print(form)
        if form.is_valid():
            form.save()
            messages.success(req, 'You have singed up successfully.')
            print("signup")
            return redirect('login')
        else:
            form = RegistrationForm()
            print("not signup")
    return render(req, "signup.html", {'form': form})
        
# <---------------|| Login & Logout ||--------------->

def log_in(req):
    if req.method == "POST":
        print("yes")
        form = LoginForm(request=req, data=req.POST)
        if form.is_valid():
            print("form valid")
            user = form.get_user()
            print("user is valid")
            if user is not None:
                login(req, user)
                print("login")
                return redirect('blood_available')
            else:
                messages.error(req, "Invalid username or password")
                print("not login")
        else:
            print("not valid")
    else:
        form = LoginForm()
        print("no")

    return render(req, "login.html", {"form": form})

@login_required(login_url='login')
def log_out(req):
    logout(req)
    return redirect('login')





@login_required(login_url='login')
def profile(req):
    print(timezone.now)
    return render(req, "profile.html")
