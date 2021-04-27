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
    path('',views.dashboard ,name="Student_dashboard"),
    path('Signin/',views.Signin ,name="Student_Signin"),
    path('Course/',views.courses ,name="Student_courses"),
    path('Assignments/',views.Assignment ,name="Student_assignments"),
    path('Quiz/',views.Quizzes ,name="Student_quizzes"),
    path('Papers/',views.Papers ,name="Student_papers"),
    path('Forms/',views.Forms ,name="Student_Forms"),    
    path('FormSubmitted/',views.FormSubmitted ,name="FormSubmitted"),    
    path('Results/',views.results ,name="Student_results"),
    path('Students/',views.students ,name="Student_students"),
    path('api/',views.api ,name="api"),
    re_path(r'.+',views.dashboard),
    
]
