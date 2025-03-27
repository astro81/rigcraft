from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuildViewSet

router = DefaultRouter()
router.register('builds', BuildViewSet, basename='build')

urlpatterns = [
    path('', include(router.urls)),
]

