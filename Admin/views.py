from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.db import connection,transaction
from Database.views import Dashboard,Get_Results,get_AssignCourses,Get_Courses,Add_Courses,\
    Teacher_Signup,Get_Teachers,Delete_Teachers,Update_Teachers,Students_Signup,\
        Get_Students,Delete_Student,Update_Student,Assign_courses,\
            Delete_Assign_Course,Delete_Courses,get_Exams,\
                get_student_courses,Assign_course_student,get_teacher_subject,\
                Delete_Student_Courses,Ocr_Mode,_get_result_subject_Admin,Get_Results_Admin
from Database.forms import Assign_Course,_StudentSubject
from django.contrib.sessions.models import Session


def Auth(request):
    session_key=request.session._session_key
    try:
        if session_key is not None:
            print("_________________________________________________________")
            session = Session.objects.get(session_key=session_key)
            session_data = session.get_decoded()
            if session_data['req']=='Admin':
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
        return render(request,'Admin/dashboard.html',{"data":Dashboard(),"LoadData":_get_result_subject_Admin(),"head":data[1]})
    else:
        return redirect('/Login')



def exams(request):
    data=Auth(request)
    if data:
        return render(request,'Admin/exams.html',{"Exams_table":get_Exams(),"head":data[1]})
    else:
        return redirect('/')



def AddCourses(request):
    data=Auth(request)
    if data:
        if request.method=="POST":
            Add_Courses(request)
        return render(request,'Admin/add_course.html',{'Courses_table':Get_Courses(),"head":data[1]})
    else:
        return redirect('/')


def AddStudentCourses(request):
    data=Auth(request)
    if data:
        if request.method=="POST":
            Assign_course_student(request)
        return render(request,'Admin/add_student_course.html',{"form":_StudentSubject(),"Student_Courses_table":get_student_courses(),"head":data[1]})
    else:
        return redirect('/')




def results(request):
    data=Auth(request)
    if data:
        return render(request,'Admin/results.html',{'Result_table':Get_Results_Admin(),"head":data[1]})
    else:
        return redirect('/')



def students(request):
    data=Auth(request)
    if data:
        if request.method=="POST":
            Students_Signup(request)
        return render(request,'Admin/students.html',{'Students_table':Get_Students(),"head":data[1]})
    else:
        return redirect('/')



def teachers(request): 
    data=Auth(request)
    if data:
        if request.method=="POST":
            Teacher_Signup(request)
        return render(request,'Admin/teachers.html',{'Teachers_table':Get_Teachers(),"head":data[1]})
    else:
        return redirect('/')



def courses(request):
    data=Auth(request)
    if data:
        if request.method=="POST":
            Assign_courses(request)
        return render(request,'Admin/courses.html' , {"form":Assign_Course(),"Assign_courses":get_AssignCourses(),"head":data[1]})
    else:
        return redirect('/')




def api(request):
    data=Auth(request)
    if data:
        if request.method=="POST":
            if request.POST["req"] =="Tdelete":
                print(Delete_Teachers(request))
            if request.POST["req"] =="Tupdate":
                print(Update_Teachers(request))
            if request.POST["req"] =="Sdelete":
                print(Delete_Student(request))
            if request.POST["req"] =="Supdate":
                print(Update_Student(request))
            if request.POST["req"] =="Cdelete":
                print(Delete_Assign_Course(request))
            if request.POST["req"] =="Course_delete":
                print(Delete_Courses(request))
            if request.POST["req"] =="delete_student_course":
                print(Delete_Student_Courses(request))
            if request.POST['req'] == "ocr_mode":
                print(Ocr_Mode(request))
            if request.POST['req'] == "signout":
                delsession(request)
                print("-> Signout <-")




        return render(request,'Admin/API.html')
    else:
        return redirect('/')
