from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blood_available, name="blood_available"),
    path('Donations/', views.donations, name="donations"),
    path('Donations/submit', views.insert_donation, name="insert_donation"),
    path('Requests/', views.requests, name="requests"),
    path('Profile/', views.profile, name="profile"),
    # path('Logout/', views.logout, name="logout"),
]