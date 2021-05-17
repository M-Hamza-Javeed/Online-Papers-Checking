from django.db import models
from Database.models import Courses
from django import forms


def file_extension(value):
    file_name=str(value).split('.')
    exe=file_name[len(file_name)-1]
    if exe in ["w2v"]:
        print("correct file")
    else:
        raise forms.ValidationError("Not allowed filetype!. upload [w2v] file")


class WModels(models.Model):
    subj = models.ForeignKey(Courses, models.DO_NOTHING, db_column='subj')     
    file = models.FileField(blank=False, null=False,upload_to='models',validators =[file_extension])

