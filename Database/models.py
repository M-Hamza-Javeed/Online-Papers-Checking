from django.db import models


class Admin(models.Model):
    name = models.CharField(db_column='Name', max_length=60)  
    email = models.EmailField(db_column='Email', primary_key=True, max_length=50)  
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True,max_length=15)  
    password = models.CharField(db_column='Password', max_length=50)  

    class Meta:
        db_table = 'admin'


class Courses(models.Model):
    subject = models.CharField(db_column='Subject', primary_key=True, max_length=60)  
    credit_hours = models.IntegerField()

    class Meta:
        db_table = 'courses'


class Teacher(models.Model):
    name = models.CharField(db_column='Name', max_length=60)  
    email = models.EmailField(db_column='Email',unique=True, primary_key=True, max_length=50)  
    phonenumber = models.CharField(db_column='PhoneNumber', unique=True, max_length=15)  
    password = models.CharField(db_column='Password', max_length=50)  
    tdate = models.DateField(db_column='TDate')  

    class Meta:
        db_table = 'teacher'


class Exam(models.Model):
    email = models.ForeignKey(Teacher,on_delete=models.CASCADE,db_column='Email')     
    examid = models.IntegerField(db_column='Examid', primary_key=True)  
    pdate = models.DateField(db_column='PDate')  
    ptime = models.TimeField(db_column='PTime')  
    time_duration = models.IntegerField(db_column='Time_duration')  

    class Meta:
        db_table = 'exam'


class ExamMcqsChoice(models.Model):
    mquestion = models.ForeignKey('ExamMcqs',on_delete = models.CASCADE,db_column='MQuestion')  
    choice = models.CharField(db_column='Choice', max_length=300)  

    class Meta:
        db_table = 'exam__mcqs_choice'


class ExamMcqs(models.Model):
    subject = models.CharField(db_column='Subject', max_length=60)  
    mquestion = models.CharField(db_column='MQuestion', primary_key=True, max_length=250)  
    examid = models.ForeignKey(Exam,on_delete = models.CASCADE,db_column='Examid')  
    manswer = models.TextField(db_column='MAnswer')  
    point = models.IntegerField(db_column='Point')  

    class Meta:
        db_table = 'exam_mcqs'
        unique_together = (('mquestion','subject','examid'),)


class ExamQuestions(models.Model):
    subject = models.CharField(db_column='Subject', max_length=60)  
    question = models.CharField(db_column='Question', primary_key=True, max_length=250)  
    keywords = models.CharField(db_column='keywords', max_length=240)  
    examid = models.ForeignKey(Exam,on_delete = models.CASCADE,db_column='Examid')  
    answer = models.TextField(db_column='Answer')  
    point = models.IntegerField(db_column='Point')  
    submit = models.BooleanField(db_column='submit',default=True)  

    class Meta:
        db_table = 'exam_questions'


class ExamScanPaper(models.Model):
    regno = models.ForeignKey('Student',on_delete = models.CASCADE,db_column='RegNo')  
    examid = models.ForeignKey(Exam,on_delete = models.CASCADE, db_column='Examid')  
    question = models.ForeignKey(ExamQuestions,on_delete = models.CASCADE, db_column='Question')  
    answer = models.TextField(db_column='Answer')  

    class Meta:
        db_table = 'exam_scan_paper'
        unique_together = (('regno', 'question','examid'),)


class ExamStudentAnswer(models.Model):
    Examid = models.ForeignKey(Exam,on_delete = models.CASCADE,db_column='Examid',default='null')  
    regno = models.ForeignKey('Student',on_delete = models.CASCADE, db_column='RegNo')  
    question = models.ForeignKey(ExamQuestions,on_delete = models.CASCADE,db_column='Question')  
    answer = models.TextField(db_column='Answer')  

    class Meta:
        db_table = 'exam_student_answer'
        unique_together = (('regno', 'question','Examid'),)


class ExamStudentMcqs(models.Model):
    Examid = models.ForeignKey(Exam,on_delete = models.CASCADE, db_column='Examid',default='null')  
    mquestion = models.ForeignKey(ExamMcqs,on_delete = models.CASCADE, db_column='MQuestion')  
    regno = models.ForeignKey('Student',on_delete = models.CASCADE, db_column='RegNo')  
    manswer = models.TextField(db_column='MAnswer')  

    class Meta:
        db_table = 'exam_student_mcqs'
        unique_together = (('regno', 'mquestion','Examid'),)


class quiz_assignment_id(models.Model):
    email = models.ForeignKey(Teacher,on_delete = models.CASCADE, db_column='Email')     
    uniqueid = models.IntegerField(db_column='Uniqueid', primary_key=True)  
    pdate = models.DateField(db_column='PDate')  
    req = models.CharField(db_column='Req',max_length=10)  

    class Meta:
        db_table = 'quiz_assignment_id'



class Mcqs(models.Model):
    uniqueid = models.ForeignKey(quiz_assignment_id,on_delete = models.CASCADE,db_column='Uniqueid')  
    subject = models.CharField(db_column='Subject', max_length=60)  
    mquestion = models.CharField(db_column='MQuestion', primary_key=True, max_length=250)  
    manswer = models.CharField(db_column='MAnswer',max_length=240)  
    point = models.IntegerField(db_column='Point')  
    mdate = models.DateField(db_column='Mdate')  

    class Meta:
        db_table = 'mcqs'



class McqsChoice(models.Model):
    mquestion = models.ForeignKey(Mcqs,on_delete = models.CASCADE, db_column='MQuestion')  
    choice = models.CharField(db_column='Choice', max_length=300)  

    class Meta:
        db_table = 'mcqs_choice'



class Questions(models.Model):
    uniqueid = models.ForeignKey(quiz_assignment_id,on_delete = models.CASCADE,db_column='Uniqueid')  
    subject = models.CharField(db_column='Subject', max_length=60)  
    question = models.CharField(db_column='Question', primary_key=True, max_length=250)  
    keywords = models.CharField(db_column='keywords', max_length=240)  
    answer = models.TextField(db_column='Answer')  
    point = models.IntegerField(db_column='Point')  

    class Meta:
        db_table = 'questions'


class ResultStubject(models.Model):
    regno    = models.ForeignKey('Student', on_delete = models.CASCADE, db_column='RegNo')  
    subject  = models.ForeignKey('Courses', on_delete = models.CASCADE, db_column='Subject')  
    uniqueid = models.ForeignKey(quiz_assignment_id,on_delete = models.CASCADE,db_column='Uniqueid',blank=True,null=True)  
    Examid   = models.ForeignKey(Exam,on_delete = models.CASCADE, db_column='Examid', blank =True,null=True)
    marks    = models.FloatField(db_column='Marks')
    tmarks   = models.FloatField(db_column='Total_Marks')  
    percentage = models.FloatField(db_column='Percentage')  

    class Meta:
        db_table = 'result_stubject'
        unique_together = (
        ('regno', 'subject','uniqueid','marks'),
        ('regno', 'subject','Examid','marks'),
        )



class Student(models.Model):
    name = models.CharField(db_column='Name', max_length=60)  
    regno = models.CharField(db_column='RegNo', primary_key=True, max_length=50)  
    password = models.CharField(db_column='Password', max_length=50)  
    sdate = models.DateField(db_column='SDate')  

    class Meta:
        db_table = 'student'


class StudentAnswer(models.Model):
    uniqueid = models.ForeignKey(quiz_assignment_id,on_delete = models.CASCADE,db_column='Uniqueid')  
    regno = models.ForeignKey(Student,on_delete = models.CASCADE, db_column='RegNo')  
    question = models.ForeignKey(Questions,on_delete = models.CASCADE, db_column='Question')  
    answer = models.TextField(db_column='Answer')  

    class Meta:
        db_table = 'student_answer'
        unique_together = (('regno', 'question','uniqueid'),)


class StudentMcqs(models.Model):
    uniqueid = models.ForeignKey(quiz_assignment_id,on_delete = models.CASCADE,db_column='Uniqueid')  
    mquestion = models.ForeignKey(Mcqs,on_delete = models.CASCADE, db_column='MQuestion')  
    regno = models.ForeignKey(Student,on_delete = models.CASCADE, db_column='RegNo')  
    manswer = models.TextField(db_column='MAnswer')  

    class Meta:
        db_table = 'student_mcqs'
        unique_together = (('regno', 'mquestion','uniqueid'),)


class StudentSubject(models.Model):
    regno = models.ForeignKey(Student,on_delete = models.CASCADE, db_column='RegNo', blank=False, default='')  
    subject = models.ForeignKey('courses',on_delete = models.CASCADE, db_column='Subject',blank=False, default='')  

    class Meta:
        db_table = 'student_subject'
        unique_together = (('regno', 'subject'),)




class TeacherSubject(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  
    email = models.ForeignKey(Teacher,on_delete = models.CASCADE, db_column='Email')  
    subject = models.ForeignKey(Courses,on_delete = models.CASCADE, db_column='Subject')  

    class Meta:
        db_table = 'teacher_subject'


class ContactUS(models.Model):
    name = models.CharField(db_column='Name', max_length=50)
    email = models.CharField(db_column='Email', max_length=50)
    message = models.TextField(db_column='Message')

    class Meta:
        db_table = 'ContactUS'
        unique_together = (('name', 'email','message'),)

