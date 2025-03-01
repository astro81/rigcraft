from django.urls import path
from component_category.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('component_category', CategoryViewSet, basename = 'category')
urlpatterns = router.urls
