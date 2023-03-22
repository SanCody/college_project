from django.db import models
from django.db.models import Sum


# Create your models here.
class Donor_Detail(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=15)
    address = models.TextField(max_length=500)
    date = models.DateField()
    blood = models.CharField(max_length=10,)
    volume = models.FloatField(default=0)

    class Meta():
        db_table="donor_detail"

    def __str__(self):
        return self.name

    # def get_total_volume(self):
    #     try:
    #         total_donation = Donor_Detail.objects.filter(blood = self.blood).aggregate(Sum('volume'))
    #         if total_donation is None:
    #             total_donation = 0
    #     except:
    #         total_donation = 0
    #     return total_donation

class Patient_Detail(models.Model):
    patientName = models.CharField(max_length=200)
    patientAge = models.CharField(max_length=5)
    patientGender = models.CharField(max_length=10)
    patientContact = models.CharField(max_length=15)
    patientBlood = models.CharField(max_length=10)
    patientBloodVolume = models.FloatField()
    patientPhysician = models.CharField(max_length=200)
    patientStatus = models.CharField(max_length=50)
    patientRequestDate = models.DateField()
    patientRequisitionDate = models.DateField()

    class Meta():
        db_table= "patient_detail"
    
