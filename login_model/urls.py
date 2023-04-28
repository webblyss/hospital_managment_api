from django.urls import path
from .views import LoginView,UserInfoView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('user_info/', UserInfoView.as_view(), name='user_info'),
]
