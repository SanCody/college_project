# Generated by Django 4.1.7 on 2023-03-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS_App', '0003_alter_patient_detail_patientrequestdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_detail',
            name='patientRequestDate',
            field=models.DateField(),
        ),
    ]
