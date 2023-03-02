from django.shortcuts import render

# Create your views here.
def blood_available(req):

    return render(req, "blood_available.html")

def donations(req):
    return render(req, "donations.html")

def requests(req):
    return render(req, "requests.html")

def profile(req):
    return render(req, "profile.html")

# def logout(req):
#     return render(req, "")

