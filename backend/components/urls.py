from django.urls import path
from components.views import ComponentCpuViewSet, ComponentMemoryViewSet, ComponentGpuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('components/cpu', ComponentCpuViewSet, basename = 'cpu')
router.register('components/memory', ComponentMemoryViewSet, basename = 'memory')
router.register('components/gpu', ComponentGpuViewSet, basename = 'gpu')

urlpatterns = router.urls

