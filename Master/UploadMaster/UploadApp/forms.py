from .models import EmployeeSheet, UploadMasterForProject, User, UploadMasterForEmployee
from django import forms
from .choices import month,project
from django.utils.translation import ugettext_lazy as _



class EmployeeSheetForm(forms.ModelForm):
    Date = forms.DateField(input_formats=['%Y-%m-%d'],widget=forms.DateInput(attrs={
            'class': 'datetimepicker-input form-control',
            'data-target': '#datetimepicker1',
            'id':"id_date",
            'placeholder':'Date'
        }))
    Task_description = forms.CharField(label='Task Description',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Description'}))
    Remark = forms.CharField(label='Remark',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Remark'}))
    Spent_Time = forms.CharField(label='Spent Time',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spent Time'}))
    # project = forms.CharField(label='project',
    #                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'project'}))
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    # client = forms.CharField(label='client',
    #                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'client'}))
    Module = forms.CharField(label='Module',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Module'}))

    # sheet = forms.FileField(label='sheet',
    #                         widget=forms.FileField(attrs={'class':'control', 'placeholder':'sheet'}))


    class Meta:
        model = EmployeeSheet
        fields = ['Task_description', 'Remark','Date', 'Spent_Time', 'project', 'client', 'Module',]


class EmployeeSheetUploadForm(forms.ModelForm):
    class Meta:
        model = EmployeeSheet
        fields = ['sheet']


class AddEmployeeForm(forms.ModelForm):
    employee_name = forms.CharField(label='Employee Name',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee Name'}))
    class Meta:
        model = UploadMasterForEmployee
        fields = ['employee_name']

class UpdateDetailsForm(forms.Form):
 excel_file = forms.FileField(label='Excel File',required=False)


class BasicUploadForm(forms.ModelForm):
    Month_calendar = forms.ChoiceField(label='month', choices=month)
    sheet = forms.FileField(label=_('File'),widget=forms.FileInput(attrs={'id': 'yz',  'class': 'for_word'}))

    class Meta:
        model = EmployeeSheet
        fields = ('Month_calendar','sheet',)


class BulkUploadForm(forms.Form):
    month = forms.ChoiceField(label='month', choices=month)
    #project = forms.ChoiceField(label='project', choices=project)
    bulk_upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class monthForm(forms.Form):
    month = forms.ChoiceField(label='month', choices=month)
