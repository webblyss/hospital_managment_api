from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ("MALE","MALE"),
    ("FEMALE","FEMALE"),
    ("OTHER","OTHER"),
)


class PatientRegistration(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100,null=True,blank=True)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField() 
    NHIS = models.CharField(max_length=100)
    vitals_checked = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) -> str:
        return f'{self.firstName} {self.lastName}'



