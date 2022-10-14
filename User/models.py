from multiprocessing.connection import answer_challenge
from optparse import Option
from django.db import models

# Create your models here.
class Student(models.Model):
    email=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,null=True,blank=True)   
    password=models.CharField(max_length=50)

class result(models.Model):
    email=models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    totalmarks=models.CharField(max_length=100)