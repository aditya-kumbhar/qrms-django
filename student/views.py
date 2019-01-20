from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return redirect('/student/home')

@login_required()
def courses(request):
    return render(request,'student/student_course.html')

@login_required()
def home(request):
    print(request.user.username)
    return render(request,"student/student_home.html")
