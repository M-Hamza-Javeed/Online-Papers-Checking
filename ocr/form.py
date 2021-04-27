from django import forms   
from .models import OCRFILES

class OCR_FORM(forms.ModelForm): 
    class Meta: 
        model = OCRFILES 
        fields = "__all__"