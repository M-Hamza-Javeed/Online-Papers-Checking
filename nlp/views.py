from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response 
from rest_framework import status
from .serializers import nlp , WModels
from .nlp import simalarity
from django.conf import settings


class NLP(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class=nlp
    
    def post(self, request, *args, **kwargs):
        data = nlp(data=request.data)
        if data.is_valid():
            output=simalarity(data.data['String_1'],data.data['String_2'])
            return Response({"Input Data ":data.data,"Ouput Data":output}, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        data = nlp(data=request.data)
        if data.is_valid():
            simalarity(data.data['String_1'],data.data['String_2'])
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)




class Models(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class=WModels
    
    def post(self, request,*args, **kwargs):
        data = WModels(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,*args, **kwargs):
        data = WModels(data=request.data)
        if data.is_valid():
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)




