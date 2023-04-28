from django.urls import path

from .views import ConsultationViews


urlpatterns = [
    path("",ConsultationViews.as_view(),name="consultation")
]




