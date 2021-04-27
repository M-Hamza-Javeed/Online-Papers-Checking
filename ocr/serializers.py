from rest_framework import serializers
from .models import OCRFILES


class OCR_FILE(serializers.ModelSerializer):
    class Meta():
        model = OCRFILES
        fields = '__all__'

