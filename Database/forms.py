from django import forms   
from .models import Admin,Student,Teacher,Courses,TeacherSubject,Exam,Mcqs,McqsChoice,StudentSubject,ContactUS

class Admin_Auth(forms.ModelForm): 
    class Meta: 
        model = Admin 
        fields = "__all__"

class Student_Auth(forms.ModelForm): 
    class Meta: 
        model = Student 
        fields = "__all__"

class Teacher_Auth(forms.ModelForm): 
    class Meta: 
        model = Teacher 
        fields = "__all__"

class Add_Course(forms.ModelForm): 
    class Meta: 
        model = Courses 
        fields = "__all__"
        

class Assign_Course(forms.ModelForm): 
    class Meta: 
        model = TeacherSubject 
        fields = "__all__"

class Exams(forms.ModelForm): 
    class Meta: 
        model = Exam 
        fields = "__all__"

class _Mcqs(forms.ModelForm):
    class Meta: 
        model = Mcqs 
        fields = "__all__"

class _McqsChoice(forms.ModelForm):
    class Meta: 
        model = McqsChoice 
        fields = "__all__"

class _StudentSubject(forms.ModelForm):
    class Meta: 
        model = StudentSubject 
        fields = '__all__'

class _ContactUs(forms.ModelForm):
    class Meta: 
        model = ContactUS 
        fields = '__all__'
    
    name=forms.CharField( widget=forms.TextInput({'placeholder':'Enter your Name'}) )
    email=forms.CharField( widget=forms.TextInput({'placeholder':'Enter your Email'}) )
    