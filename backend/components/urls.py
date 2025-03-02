from django.urls import path
from components.views import ComponentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('components/cpu', ComponentViewSet, basename = 'cpu')
urlpatterns = router.urls