from django.shortcuts import render
from .models import Consultation
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ConsultationSerializers
# Create your views here.


class ConsultationViews(APIView):
    def get(self,request):
        patient = Consultation.objects.all()
        serializer  = ConsultationSerializers(patient,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = ConsultationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






