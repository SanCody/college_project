from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.blood_available, name="blood_available"),
    # path('Blood Available/A+', views.BloodAv, name="A+"),
    path('Blood Available/<str:blood>', views.BloodAv, name="bType"),

    # Donations
    path('Donations/', views.donations, name="donations"),
    path('viewDonation/<int:id>', views.viewDonor, name="viewDonation"),
    path('updateDonor/<int:id>', views.update_donor, name="updateDonor"),
    path('deleteDonor/<int:id>', views.delete_donor, name="deleteDonor"),

    # Requests
    path('Requests/', views.requests, name="requests"),
    path('viewPatient/<int:id>', views.viewPatient, name="viewPatient"),
    path('updatePatient/<int:id>', views.update_patient, name="updatepatient"),
    path('deletePatient/<int:id>', views.delete_patient, name="deletePatient"),

    
    # path('Logout/', views.logout, name="logout"),
    path('Profile/', views.profile, name="profile"),
]