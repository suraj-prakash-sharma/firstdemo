from django.db import models
from django.db.models.base import Model

# Create your models here.
class student(models.Model):
    stu_id=models.IntegerField()
    stu_name=models.CharField(max_length=40)
    stu_mail=models.CharField(max_length=40)

def __str__(self):
    return self.stu_name