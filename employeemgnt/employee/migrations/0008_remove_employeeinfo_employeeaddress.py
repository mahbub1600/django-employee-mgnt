# Generated by Django 3.1.2 on 2020-11-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20201105_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeinfo',
            name='employeeAddress',
        ),
    ]
