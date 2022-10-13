"""quizproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Adminlogin/", views.Admin_login,name="Admin_login"),
    path('saveas/',views.saveas,name="saveas"),
    path('verify/',views.login_verify,name="verify"),
    path('Admindashboard/',views.Admin_dashboard,name="Admin_dashboard"),
    path('Adminstudent/',views.Admin_student,name="Admin_student"),
    path('ViewStudent/',views.Admin_view_student, name="Admin_view_Student"),
    path("edit/<id>",views.edit,name="Admin_student_edit"),
    path("update/",views.update,name="update"),
    path('Admincourse/',views.Admin_course,name="Admin_course"),
    path('Addcourse/',views.Add_course,name="Addcourse"),
    path('saveCourse/', views.saveCourse, name="Save_course"),
    path('Viewcourse/',views.Viewcourse,name="Viewcourse"),
    path('Adminbase/',views.Admin_base,name="Admin_base"),
    path('Adminquestion/',views.Admin_question,name="Admin_question"),
    path('Addquestion/',views.Add_question,name="Addquestion"),
    path('Viewquestion/',views.Viewquestion,name="Viewquestion"),
    path('saveQuestion/', views.saveQuestion, name="Save_question"),
    path('AdminViewquestion/<course>',views.Admin_view_question,name="Admin_view_question"),
    path('AdminStudentmarks/',views.Admin_student_marks,name="Admin_student_marks"),
    path('AdminViewmarks/<email>',views.Admin_view_marks,name="Admin_view_marks"),
    path('delete/<id>',views.delete,name="deletequestion"),
    path('deleteStudent/<id>',views.deleteStudent,name="deleteStudent"),
]
