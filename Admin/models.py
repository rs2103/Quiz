from django.db import models

# Create your models here.
class Admin(models.Model):
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Subject(models.Model):
    course = models.CharField(max_length=100)
    totalquestion=models.CharField(max_length=100,default='')
    totalmarks=models.CharField(max_length=100,null=True,blank=True)

class AddQuestion(models.Model):
    course = models.CharField(max_length=100,default='')
    marks = models.CharField(max_length=100,null=True,blank=True)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)