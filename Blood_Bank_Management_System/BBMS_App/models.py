from django.db import models

# Create your models here.
class Donor_Detail(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    address = models.TextField(max_length=500)
    date = models.DateField()
    blood = models.CharField(max_length=10,)
    volume = models.FloatField(default=0)

    class Meta():
        db_table="donor_detail"
