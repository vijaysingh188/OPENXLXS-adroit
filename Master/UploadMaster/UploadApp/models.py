from django.db import models
from .choices import month


class UploadMasterForProject(models.Model):
    Project = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Project


class UploadMasterForClient(models.Model):
    client_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.client_name


class UploadMasterForEmployee(models.Model):
    employee_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.employee_name)


def directory_path(instance, filename):
    if filename:
        ans = filename.split('.')[-1]
    return 'Myfiles/{0}/{1}/{2}'.format(instance.employee_name, instance.Date, filename)


class EmployeeSheet(models.Model):
    employee_name = models.ForeignKey(UploadMasterForEmployee, null=False, blank=False, on_delete=models.CASCADE)
    Date = models.DateField(null=True, blank=True)
    Task_description = models.CharField(max_length=100,null=True, blank=True)
    Remark = models.CharField(max_length=100,null=True, blank=True)
    Spent_Time =models.CharField(max_length=50,null=True, blank=True)
    project = models.ForeignKey(UploadMasterForProject, null=True, blank=True, on_delete=models.CASCADE)
    client = models.ForeignKey(UploadMasterForClient, null=True, blank=True, on_delete=models.CASCADE)
    Module = models.CharField(max_length=100, blank=True, null=True)
    sheet = models.FileField(upload_to=directory_path)
    Month_calendar = models.CharField(max_length=30,null=True)

    def __str__(self):
        return str(self.employee_name)


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username







