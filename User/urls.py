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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('AboutUs/',views.AboutUs,name="AboutUs"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('registration/', views.registration,name="registration"),
    path('Studentbase/',views.Student_base,name="Student_base"),
    path('Question/<course>', views.Question,name="Question"),
    path('Studentdashboard/', views.Student_dashboard,name="Student_dashboard"),
    path('ViewQuiz/',views.ViewQuiz,name="ViewQuiz"),
    path('Studentexam/',views.Student_exam,name="Student_exam"),
    path('Studentviewquiz/', views.Student_view_quiz,name="Student_view_quiz"),
    path('save/',views.save,name="save"),
    path('verification/',views.login_verification,name="verification"),
    path('displayQuestion/<course>',views.displayQuestion,name="displayQuestion"),
    path('saveMarks/',views.saveMarks,name="saveMarks"),
    path('displayMarks/',views.displayMarks,name="displayMarks"),
    path('ViewMarks/',views.ViewMarks,name="ViewMarks"),
    path('Studentviewmarks/', views.Student_view_marks,name="Student_view_marks"),
    path('forgot_password/',views.forgot_password,name="forgotpassword"),
    path('edit/',views.edit,name="edit"),
    path('checkExamSubject/',views.checkExamSubject,name="checkExamSubject"),
]
urlpatterns += staticfiles_urlpatterns()
