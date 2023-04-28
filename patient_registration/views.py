from django.shortcuts import render
from .models import PatientRegistration
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PatientRegistrationSerializers
# Create your views here.


class PatientRegistrationView(APIView):
    def get(self,request):
        patient = PatientRegistration.objects.all()
        serializer  = PatientRegistrationSerializers(patient,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = PatientRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






