from django.contrib import admin
import hashlib

from .models import UploadMasterForProject, EmployeeSheet, UploadMasterForClient,User

admin.site.register(UploadMasterForProject)
admin.site.register(UploadMasterForClient)
admin.site.register(EmployeeSheet)
admin.site.register(User)


