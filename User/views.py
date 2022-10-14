import imp
from urllib import response
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from Admin.models import Subject,AddQuestion
from User.models import result
from django.core import serializers
from django.http import HttpResponse

from User.models import Student
# from .forms import NewUserForm
# from django.contrib.auth import login
# Create your views here.
def home(req):
    return render(req,'home.html')
def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return render(req,'home.html')

def login(req):
    storage = messages.get_messages(req)
    storage.used = True
    return render(req,'login.html')
def registration(req):
    return render(req,'registration.html')
def Student_base(req):
    return render(req,'Student_base.html')

def Student_dashboard(req): 
    return render(req,'Student_dashboard.html')

def AboutUs(req):
    return render(req,'AboutUs.html')

def save(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['repeatpassword']
        username=email

        if password==confirm_password:
            if Student.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(registration)
            else:
                user = Student.objects.create( email=email,first_name=first_name, last_name=last_name,password=password)
                return redirect(login)


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(registration)
            

    else:
        return render(request, 'registeration.html')

def login_verification(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        storage = messages.get_messages(request)
        storage.used = True

        user = Student.objects.filter(email=email, password=password)

        if len(user) > 0:
            request.session['email'] = email
            return redirect('Student_dashboard')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request, '')

def ViewQuiz(req):
    allSubjects = Subject.objects.all()
    data = {"allSubjects": list(allSubjects)}
    return render(req, 'ViewQuiz.html', data)

def Student_exam(req): 
    return render(req,'Student_exam.html')

def Student_view_quiz(req):
    email = req.session.get('email') 
    allSubjects = Subject.objects.all()
    data = {"allsubjects": list(allSubjects), "email": email}
    return render(req,'Student_view_quiz.html', data) 

def Question(req, course):
    email = req.session.get('email')
    data = {"course": course, "email": email}
    return render(req, 'Question.html', data)


def displayQuestion(req, course):
    allQuestions = AddQuestion.objects.filter(course=course)
    qs_json = serializers.serialize('json', allQuestions)
    return HttpResponse(qs_json, content_type='application/json')

def checkExamSubject(req):
    email = req.POST['email'] 
    course = req.POST['course']
    obj = result.objects.filter(email=email, course=course)
    if len(obj) > 0:
        data = "1"
    else:
        data ="0"
    return HttpResponse(data)

def saveMarks(req):    
    totalmarks = req.GET['totalmarks']
    course = req.GET['course']
    email=req.GET['email']
    marks=result.objects.create(totalmarks=totalmarks,course=course,email=email)
    return HttpResponse("Sucess")
    

def displayMarks(req,email):
    allMarks = result.objects.filter(email=email)
    marks_json = serializers.serialize('json', allMarks)
    return HttpResponse(marks_json, content_type='application/json')

def Student_view_marks(req):
    email = req.session.get('email')
    allMarks= result.objects.filter(email=email)
    data = {"allMarks": list(allMarks)}
    return render(req, 'Student_view_marks.html',data)  
  

def ViewMarks(req): 
    email = req.session.get('email')
    allMarks= result.objects.filter(email=email)
    data = {"allMarks": list(allMarks)}
    return render(req, 'Result.html', data)


def forgot_password(req):
    return render(req,'forgot_password.html')

def edit(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        repeatpassword=request.POST['repeatpassword']

        storage = messages.get_messages(request)
        storage.used = True

        if password == repeatpassword:
            if Student.objects.filter(email=email).exists():
                    user=Student.objects.get(email=email)
                    user.password=password
                    user.save()
                    messages.info(request, 'You have successfully changed your password')
                    return redirect(forgot_password)

            else:
                messages.info(request,'Entered email does not exists')
                return render(request,'forgot_password.html')
        else:
            messages.info(request,'Both Password is Not Matched')
            return render(request,'forgot_password.html')
    
    else:
        return redirect('login.html')
    



 

    