
from .models import PatientRegistration
from rest_framework import serializers


class PatientRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientRegistration
        fields = ['id','firstName','lastName','middleName','phone','email','age','gender','date_of_birth','NHIS']