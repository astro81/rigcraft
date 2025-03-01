from django.urls import path
from component_category.views import CategoryListAPIView

urlpatterns = [
    path('component_category/', CategoryListAPIView.as_view())  # /api/category
]
