# Generated by Django 2.1.5 on 2020-02-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeesheet',
            name='Month',
            field=models.CharField(max_length=30, null=True),
        ),
    ]