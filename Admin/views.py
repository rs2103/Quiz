from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Admin,Subject,AddQuestion
from User.models import result, Student

# Create your views here.
def Admin_login(req):
    return render(req,'Admin_login.html')
def Admin_dashboard(req):
    return render(req,'Admin_dashboard.html')

def Admin_base(req):
    return render(req,'Admin_base.html')

def saveas(req):
    emailid = req.POST['emailid']
    password = req.POST['password']

    response=Admin.objects.create(emailid=emailid,password=password)
    if response.id>0:
        message={"message":"Login Successfull"}
    else:
        message={"message":"Login Failed"}
        

    data={"message":message}
    return render(req,"Admin_login.html",data)

def logout(req):
    try:
        del req.session['email']
    except KeyError:
        pass
    return render(req,'home.html')

def login_verify(request):
    if request.method == 'POST':
        emailid = request.POST['emailid']
        password = request.POST['password']

        admins = Admin.objects.filter(emailid=emailid, password=password)

        if len(admins) > 0:
            request.session['emailid']=emailid
            return redirect('Admin_dashboard')
        else:
            data = {"message": 'Invalid Email or Password'}
            return render(request, 'Admin_login.html', data)

    else:
        return render(request, 'Admin_login.html')


def Admin_course(req):
    allSubjects = Subject.objects.all()
    data = {"allSubjects": list(allSubjects)}
    return render(req, 'Admin_course.html', data)

def Add_course(req):
    return render(req, 'Addcourse.html')

def saveCourse(request):
    if request.method == 'POST':
        course = request.POST['course']
        totalmarks = request.POST['totalmarks']
        totalquestion = request.POST['totalquestion']

        new_course = Subject.objects.create(course=course,totalmarks=totalmarks,totalquestion=totalquestion)
        new_course.save()
        return redirect('Admin_course')
    else:
        return render(request, 'Addcourse.html')

def Viewcourse(req):
    allSubjects = Subject.objects.all()
    data = {"allSubjects": list(allSubjects)}
    return render(req, 'Viewcourse.html', data)
def Admin_question(req):
    allQuestions = AddQuestion.objects.all()
    data = {"allQuestions": list(allQuestions)}
    return render(req,'Admin_question.html',data)

def Add_question(req):
    return render(req, 'Addquestion.html')
    

def Viewquestion(req):
    allQuestions = Subject.objects.all()
    data = {"allQuestions": list(allQuestions)}
    return render(req,'Viewquestion.html',data)

    
def saveQuestion(request):
    if request.method == 'POST':
        course = request.POST['course']
        marks = request.POST['marks']
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']

        new_question = AddQuestion.objects.create(course=course,marks=marks,question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
        new_question.save()
        return redirect('Admin_question')
    else:
        return render(request, 'Addquestion.html')

def Admin_view_question(req,course):
    allQuestions = AddQuestion.objects.filter(course=course)
    data = {"allQuestions": list(allQuestions)}
    return render(req, 'Admin_view_question.html',data)  

def Admin_student(req):
    return render(req,'Admin_student.html')

def Admin_view_student(req):
    allStudents= Student.objects.all()
    data = {"allStudents": list(allStudents)}
    return render(req,'Admin_view_student.html',data)
    

def Admin_student_marks(req):
    allStudents= Student.objects.all()
    data = {"allStudents": list(allStudents)}
    return render(req,'Admin_student_marks.html',data)

def Admin_view_marks(req,email):
    allMarks= result.objects.filter(email=email)
    data = {"allMarks": list(allMarks)}
    return render(req, 'Admin_view_marks.html', data)

def delete(req, id):
    obj = AddQuestion.objects.get(id=id)

    obj.delete()

    response = AddQuestion.objects.all()
    data = {"allQuestions": list(response), "message" : "Data Deleted"}
    
    return render(req, 'Admin_view_question.html', data)

def deleteStudent(req, id):
    obj = Student.objects.get(id=id)

    obj.delete()

    response = Student.objects.all()
    data = {"allStudents": list(response), "message" : "Data Deleted"}
    
    return render(req, 'Admin_view_student.html', data)

def edit(req,id):
    obj = Student.objects.get(id=id)
    data  = {"student": obj}
    return render(req, 'Admin_student_edit.html', data)

def update(req):
    email=req.POST['email']
    first_name=req.POST['first_name']
    last_name=req.POST['last_name']
    password=req.POST['password']
    obj = Student.objects.get(email=email)
    obj.first_name=first_name
    obj.last_name=last_name
    obj.password=password

    obj.save()
    response=Student.objects.all()
    data={"allStudents":list(response),"messege": "Data Updated"}

    return render(req,'Admin_view_student.html',data)