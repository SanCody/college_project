from django.db import models

# Create your models here.
class Donar_Detail(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=30, choices = (('Male' ,'Male'),('Female' ,'Female')))
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    address = models.TextField(max_length=500)
    date = models.DateField()
    blood = models.CharField(max_length=10, primary_key=True)
    volume = models.FloatField(default=0)

    class Meta():
        db_table="donar_detail"
