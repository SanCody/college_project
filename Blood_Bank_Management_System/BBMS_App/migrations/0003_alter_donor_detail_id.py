# Generated by Django 4.1.7 on 2023-03-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBMS_App', '0002_alter_donor_detail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor_detail',
            name='id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
    ]