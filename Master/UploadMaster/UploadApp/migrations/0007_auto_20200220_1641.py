# Generated by Django 2.1.5 on 2020-02-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UploadApp', '0006_employeesheet_sheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesheet',
            name='sheet',
            field=models.FileField(max_length=254, null=True, upload_to='documents'),
        ),
    ]
