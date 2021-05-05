"""papers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.dashboard ,name="Admin_dashboard"),
    path('Exam/' ,views.exams ,name="Admin_exams"),
    path('Add_Coruse/',views.AddCourses ,name="Admin_add_course"),
    path('Add_Student_Coruses/',views.AddStudentCourses ,name="add_student_course"),
    path('Course/',views.courses ,name="Admin_courses"),
    path('Result/',views.results ,name="Admin_results"),
    path('Student/',views.students ,name="Admin_students"),
    path('Teacher/',views.teachers ,name="Admin_teachers"),
    path('api/',views.api ,name="api"),
    re_path(r'$',views.dashboard)
]
