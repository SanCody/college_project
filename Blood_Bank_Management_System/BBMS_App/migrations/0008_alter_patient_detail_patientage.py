# Generated by Django 4.1.7 on 2023-03-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS_App', '0007_alter_patient_detail_patientrequestdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_detail',
            name='patientAge',
            field=models.CharField(max_length=5),
        ),
    ]