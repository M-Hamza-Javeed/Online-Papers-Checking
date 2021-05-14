from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection,transaction
from Database.views import Teacher_Signin,Get_Courses,create_mcqs,Get_Students,\
    create_subjective,create_exam,Dashboard,get_AssignCourses,get_Exams,Get_Results,_get_result_subject_Teacher
from django.contrib.sessions.models import Session
import json
from datetime import date


def Auth(request):
    try:
        session_key=request.session._session_key
        if session_key is not None:
            print("_________________________________________________________")
            session = Session.objects.get(session_key=session_key)
            session_data = session.get_decoded()
            if session_data['req']=='Teachers':
                print("\n Session Key   -> ", session_key)
                print("\n Session Data  -> ", session_data,"\n")
                return True,session_data
            else:
                return False
        else:
            return False
    except:
        pass
    return False


def delsession(request):
    try:
        session_key=request.session._session_key
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        for i in session_data:
            del request.session[i]
    except:
        print("error")
        pass





def dashboard(request):
    data=Auth(request)
    if data:
        return render(request,'Teachers/dashboard.html',{"Data":Dashboard(),"head":data[1],"LoadData":_get_result_subject_Teacher(data[1]['email'])})
    else:
        return redirect('/Teachers/Signin/')



def exams(request):
    data=Auth(request)
    if data:
        return render(request,'Teachers/exams.html',{"Exams_table":get_Exams(),"head":data[1]})
    else:
        return redirect('/Teachers/Signin/')



def results(request):
    data=Auth(request)
    if data:
        return render(request,'Teachers/results.html',{"Result_table":Get_Results(data[1]["email"]),"result":"","head":data[1]})
    else:
        return redirect('/Teachers/Signin/')



def students(request):
    data=Auth(request)
    if data:
        return render(request,'Teachers/students.html',{"Students_table":Get_Students(),"head":data[1]})
    else:
        return redirect('/Teachers/Signin/')



def Forms(request):
    data=Auth(request)
    if data:
        courses=Get_Courses()
        if request.method=="POST":
            return render(request,'Teachers/Papers.html',{"courses":courses,"head":data[1]})
        else:
            return render(request,'Teachers/Papers.html',{"courses":courses,"head":data[1]})
    else:
        return redirect('/Teachers/Signin/')



def courses(request):
    data=Auth(request)
    if data:
        return render(request,'Teachers/courses.html',{"Assign_courses":get_AssignCourses(data[1]["email"]),"head":data[1]})
    else:
        return redirect('/Teachers/Signin/')


def Signin(request):
    if request.method=="POST":
        if Teacher_Signin(request):
            _Session(request)
            return redirect('/Teachers/')
        else:
            return render(request,'Teachers/Signin.html',{'title':"Papers"})
    else:
        return render(request,'Teachers/Signin.html',{'title':"Papers"})



def api(request):
    print("<<<- ->>>")
    try:
        data=Auth(request)
        if request.method == "POST":
            if request.POST['req']=="mcqs":
                print(request.POST['req'])
                print(request.POST)
                create_mcqs(json.loads(request.POST['data']),data[1]["email"])
            if request.POST['req']=="subjective":
                print(request.POST['req'])
                print(request.POST)
                create_subjective(json.loads(request.POST['data']),data[1]["email"])
            if request.POST['req']=="exam":
                print(request.POST['req'])
                print(request.POST)
                create_exam(json.loads(request.POST['data']),data[1]["email"])
            if request.POST['req'] == "signout":
                delsession(request)
                print("-> Signout <-")

    except:
        pass

    return render(request,"Teachers/api.html")



def _Session(request):
    d2 = date.today().strftime("%B %d, %Y")
    request.session['email']=request.POST['email']
    request.session['req']='Teachers'
    request.session['date']=d2
    return True




