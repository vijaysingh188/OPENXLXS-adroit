from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth.views import auth_login
from django.contrib.auth.views import auth_logout
urlpatterns = [

    path('', views.login_request, name='login'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('home',views.home, name='home'),
    path('employee_data/<int:e_data>',views.employee_data, name='employee_data'),
    path('add_employee',views.add_employee, name='add_employee'),
    path('add_record/<int:e_id>', views.add_record, name='add_record'),
    #path('upload_sheet/<int:task_id>', views.upload_sheet, name='upload_sheet'),
    path('download/<int:e_id>', views.download, name='download'),
    path('edit_task/<int:k_id>', views.edit_task, name='edit_task'),
    path('bulk_upload', views.bulk_upload, name='bulk_upload'),
    path('basic_upload', views.basic_upload, name='basic_upload'),
    path('upload', views.upload, name='upload'),
    path('report',views.report,name='report'),
    path('project_wise_report',views.project_wise_report,name='project_wise_report'),
    path('user_wise_report',views.user_wise_report,name='user_wise_report'),

]