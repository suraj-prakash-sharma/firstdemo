from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class UserAdmin(admin.ModelAdmin):
    list_display=('stu_id','stu_name','stu_mail')