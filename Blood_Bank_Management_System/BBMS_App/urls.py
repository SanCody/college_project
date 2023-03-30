from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.blood_available, name="blood_available"),
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

    # Signup
    path('Signup/', views.signup, name="signup"),
    
    # Login & Logout
    path('Login/', views.log_in, name="login"),
    path('Logout/', views.log_out, name="logout"),

    # Profile
    path('Profile/', views.profile, name="profile"),
    path('chgP/', views.changePassword, name="changePassword"),
    path('EditUser/', views.changeUser, name="EditUser"),
]