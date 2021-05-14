from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection,transaction
from Database.views import Student_Signin ,Generate_Forms,get_papers,\
    student_assign_course,RegisterSubject,Student_result_subject,\
        student_quiz,student_assignments,_process_form,get_Student_data,_get_result_subject_Student
from django.contrib.sessions.models import Session
from datetime import date
import json

def Auth(request):
    try:
        session_key=request.session._session_key
        if session_key is not None:
            print("_________________________________________________________")
            session = Session.objects.get(session_key=session_key)
            session_data = session.get_decoded()
            if session_data['req']=='Students':
                print("\n Session Key   -> ", session_key)
                print("\n Session Data  -> ", session_data,"\n")
                return True,session_data
            else:
                return False
        else:
            return False
    except:
        pass



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
        print(request.session['regno'])
        return render(request,'Students/dashboard.html',{"head":data[1],"LoadData":_get_result_subject_Student(data[1]["regno"])})
    else:
        return redirect('/Students/Signin/')



def Signin(request):
    if request.method=="POST":
        if Student_Signin(request):
            print(_Session(request))
            return redirect('/Students/')
        else:
            return render(request,'Students/Signin.html',{'title':'Papers'})
    else:
        return render(request,'Students/Signin.html',{'title':'Papers'})




def results(request):
    data=Auth(request)
    if data:
        return render(request,'Students/results.html',{"head":data[1],"result_table":Student_result_subject(data[1]["regno"])})
    else:
        return redirect("/Students/Signin/")


def students(request):
    data=Auth(request)
    if data:
        return render(request,'Students/students.html',{"head":data[1]})
    else:
        return redirect("/Students/Signin/")


def teachers(request):
    data=Auth(request)
    if data:
        return render(request,'Students/teachers.html',{"head":data[1]})
    else:
        return redirect("/Students/Signin/")

def courses(request):
    data=Auth(request)
    if data:
        return render(request,'Students/courses.html',{"head":data[1],"RegisterSubject":RegisterSubject(data[1]['regno'])})
    else:
        return redirect("/Students/Signin/")


def Assignment(request):
    data=Auth(request)
    if data:
        return render(request,'Students/assignments.html',{"head":data[1], "get_assignment":student_assignments(data[1]['regno'])})
    else:
        return redirect("/Students/Signin/")



def Quizzes(request):
    data=Auth(request)
    if data:
        return render(request,'Students/quizzes.html',{"head":data[1],"get_quiz":student_quiz(data[1]['regno'])})
    else:
        return redirect("/Students/Signin/")

def Papers(request):
    data=Auth(request)
    if data:
        return render(request,'Students/papers.html',{"head":data[1],"get_papers":get_papers(data[1]['regno'])})
    else:
        return redirect("/Students/Signin/")


def Forms(request):
    data=Auth(request)
    if data:
        Generate_Form=Generate_Forms(request.GET['examid'],request.GET['req'],data[1]['regno'])
        print(Generate_Form)
        if Generate_Form['Valid']:
            return render(request,'Students/Exam.html',{"Generate_Forms":Generate_Form})
        else:
            return redirect("/Students/FormSubmitted/")
    else:
        return redirect("/Students/Signin/")



def FormSubmitted(request):
    data=Auth(request)
    if data:
        return render(request,'Students/formsubmitted.html')



def api(request):
    print("<<<- ->>>")
    data=Auth(request)
    if request.method == "POST":
        if request.POST['req']=="papers":
            if _process_form(json.loads(request.POST['data']),data[1]['regno']):
                print(1)
            else:
                print(2)
        elif request.POST['req']=="quiz":
            _process_form(json.loads(request.POST['data']),data[1]['regno'])
        elif request.POST['req']=="assignment":
            _process_form(json.loads(request.POST['data']),data[1]['regno'])

    if request.POST['req'] == "signout":
            delsession(request)
            print("-> Signout <-")

    return render(request,"Students/api.html")



def _Session(request):
    d2 = date.today().strftime("%B %d, %Y")
    request.session['regno']=request.POST['regno']
    request.session['req']='Students'
    request.session['date']=d2
    request.session['dash_data']= get_Student_data(request.POST['regno'])
    return True



