from .views import OPDView
from django.urls import path


urlpatterns =[
    path("",OPDView.as_view(),name="opd in patient")
]





