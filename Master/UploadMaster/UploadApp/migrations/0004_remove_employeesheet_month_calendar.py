# Generated by Django 2.1.5 on 2020-02-19 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UploadApp', '0003_auto_20200219_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeesheet',
            name='Month_calendar',
        ),
    ]
