from django.shortcuts import render , redirect
from django.http import HttpResponse
from Database.views import Admin_Signup , Admin_Signin, contactus
from Database.forms import _ContactUs
from Database.models import Admin
from datetime import date


def index(request):
    return render(request,'Main/index.html')

def Documentation(request):
    return render(request,'Main/Documentation.html')

def Features(request):
    return render(request,'Main/Features.html')

def Login(request):
    if request.method=="POST":
        if Admin_Signin(request):
            _Session(request)
            return redirect('/Admin/')
        else:
            return render(request,'Main/Login.html')
    else:
        return render(request,'Main/Login.html')


def Signup(request):
    if request.method=="POST":
        if Admin_Signup(request):
            _Session(request)
            return redirect('/Admin/')
        else:
            return render(request,'Main/Signup.html')
    else:
        return render(request,'Main/Signup.html')


def ContactUs(request):
    if request.method == "POST":
        contactus(request)
    return render(request,'Main/ContactUs.html',{"form":_ContactUs()})


def _Session(request):
    d2 = date.today().strftime("%B %d, %Y")
    request.session['email']=request.POST['email']
    request.session['req']='Admin'
    request.session['date']=d2
    return True

