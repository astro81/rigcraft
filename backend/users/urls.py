from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RegistrationAPIView, LoginAPIView, LogoutAPIView, UserProfileView

router = DefaultRouter()

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]