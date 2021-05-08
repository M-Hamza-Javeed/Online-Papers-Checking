from django.contrib import admin
from django.apps import apps
from .models import Admin,Student,Teacher,Courses,TeacherSubject,\
    Exam,Mcqs,McqsChoice,Questions,ExamMcqs,ExamMcqsChoice,ExamQuestions,ResultStubject


admin.site.register([Admin,Student,Teacher,Courses,TeacherSubject,
Exam,ResultStubject,Mcqs,McqsChoice,Questions,ExamMcqs,ExamMcqsChoice,ExamQuestions])