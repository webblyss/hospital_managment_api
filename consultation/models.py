from django.db import models
from OPD_ .models import OPD
# Create your models here.


WARD = (
    ("FEMALE-WARD","FEMALE-WARD"),
    ("MALE-WARD","MALE-WARD"),
    ("PEADIATRIC-WARD","PEADIATRIC-WARD"),
    ("EMERGENCY-WARD","EMERGENCY-WARD"),

)

class Consultation(models.Model):
    opd_info = models.ForeignKey(OPD,on_delete=models.CASCADE)
    patient_complains = models.TextField()
    doctor_diagnosis = models.CharField(max_length=100)
    medication = models.CharField(max_length=500)
    admitted_to_ward = models.CharField(choices=WARD,max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.opd_info.patient_info.firstName} - {self.doctor_diagnosis}'








