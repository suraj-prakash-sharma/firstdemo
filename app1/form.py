from django import forms
from django.forms import fields
#from django.core import validators
from .models import student
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=['stu_id','stu_name','stu_mail']
        labels={'stu_id':'enter ID','stu_name':'enter  name','stu_mail':'enter email'}