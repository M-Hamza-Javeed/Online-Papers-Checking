from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response 
from rest_framework import status
from .serializers import OCR_FILE
from .filters import imagefilter
from .tesseract import ExtractText



class OCR(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class=OCR_FILE


    def post(self, request, *args, **kwargs):
        key=[i for i in request.POST]
        file_serializer = OCR_FILE(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            if 'req' in  key:
                if(request.POST['req']=="noresponse"):
                    print("__---__")
                    print(request.POST)
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                ExtractText(file_serializer.data['file'])
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        file_serializer = OCR_FILE(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





