# Generated by Django 4.1.7 on 2023-03-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar_detail',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30),
        ),
        migrations.AlterModelTable(
            name='donar_detail',
            table='donar_detail',
        ),
    ]
