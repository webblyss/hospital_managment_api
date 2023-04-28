from rest_framework import serializers
from .models import OPD

class OPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = OPD
        fields = ['patient_info','temperature','pulse','respiration','bp','date']
        depth = 1

