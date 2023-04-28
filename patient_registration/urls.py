from django.urls import path
from .views import PatientRegistrationView

urlpatterns = [
    path("",PatientRegistrationView.as_view(),name="register")
]




