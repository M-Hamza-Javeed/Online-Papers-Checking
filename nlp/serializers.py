from rest_framework.serializers import  *
from rest_framework import serializers
from .models import WModels



class nlp(Serializer):
    String_1  = CharField()
    String_2  = CharField()
    class Meta:
        fields = '__all__'


class WModels(serializers.ModelSerializer):
    class Meta():
        model = WModels
        fields = '__all__'



