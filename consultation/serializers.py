from rest_framework import serializers
from .models import Consultation


class ConsultationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Consultation
        fields = ['opd_info','patient_complains','doctor_diagnosis','medication','admitted_to_ward','date']
        depth = 5








