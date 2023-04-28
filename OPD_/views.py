from django.shortcuts import render
from .models import OPD
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .seriliazers import OPDSerializer
# Create your views here.


class OPDView(APIView):
    def get(self,request):
        patient = OPD.objects.all()
        serializer  = OPDSerializer(patient,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = OPDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






