from django.db import models
from patient_registration.models import PatientRegistration
# Create your models here.


class OPD(models.Model):
    patient_info = models.ForeignKey(PatientRegistration,on_delete=models.CASCADE)
    temperature = models.DecimalField(decimal_places=2,max_digits=5)
    pulse = models.IntegerField()
    respiration = models.IntegerField()
    bp = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.patient_info.firstName}'
    





