from rest_framework.serializers import  *

class nlp(Serializer):
    String_1  = CharField()
    String_2  = CharField()
    class Meta:
        fields = '__all__'


