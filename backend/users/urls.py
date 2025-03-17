from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RegistrationAPIView
from icecream import ic

router = DefaultRouter()

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
]