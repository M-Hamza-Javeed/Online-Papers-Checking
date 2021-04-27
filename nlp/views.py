from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response 
from rest_framework import status
from .serializers import nlp
from .nlp import simalarity

class OCR(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class=nlp
    

    def post(self, request, *args, **kwargs):
        data = nlp(data=request.data)
        if data.is_valid():
            simalarity(data.data['String_1'],data.data['String_2'])
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        data = nlp(data=request.data)
        if data.is_valid():
            simalarity(data.data['String_1'],data.data['String_2'])
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)








