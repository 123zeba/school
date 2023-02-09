from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages, auth


# Create your views here.

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def message(request):
    return render(request,'message.html')
def index(request):
    program=Department.objects.all()
    d={'program':program}
    return render(request,'index.html',d)

def load_courses(request):
    department_id=request.GET.get('department')
    courses=Course.objects.filter(department_id=department_id).order_by('name')
    return render(request,'courses_dropdown_list_options.html',{'courses':courses})

def logout(request):
    auth.logout(request)
    return redirect('/')