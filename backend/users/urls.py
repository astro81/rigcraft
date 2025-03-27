# users.urls
from django.urls import path
from users.views import (
    RegistrationAPIView, 
    UserLoginAPIView, 
    UserLogoutAPIView, 
    UserProfileAPIView,
    AccountDeletionAPIView, 
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),  
    path('delete-account/', AccountDeletionAPIView.as_view(), name='delete-account'),
]

