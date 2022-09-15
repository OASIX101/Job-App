from django.contrib import admin
from .models import JobAdvert, JobApplication

@admin.register(JobAdvert)
class AdminReg(admin.ModelAdmin):
    list_display = ['job_name', 'company_name', 'employment_type', 'employment_level']



@admin.register(JobApplication)
class AdminReg(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name', 'email', 'phone']