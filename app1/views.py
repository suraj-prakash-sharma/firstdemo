from django.shortcuts import render
from django.http import HttpResponse
from firstdemo import settings
from .models import student
from .form import studentform
# Create your views here.
def show(request):
    '''stu=student.objects.all()'''
    if request.method=='POST':
        fm=studentform(request.POST)
        if fm.is_valid():
            uid=fm.cleaned_data['stu_id']
            name=fm.cleaned_data['stu_name']
            email=fm.cleaned_data['stu_mail']
            reg=student(id=1,stu_id=uid,stu_name=name,stu_mail=email)
            reg.save()
    else:
        fm=studentform()
    return render(request,'demo.html',{'form':fm})

    