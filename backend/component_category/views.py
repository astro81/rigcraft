from django.shortcuts import render
from rest_framework import generics
from component_category.models import ComponentCategoryModel
from component_category.serializers import ComponentCategorySerializer

# Create your views here.

class CategoryListAPIView(generics.ListAPIView):
    queryset = ComponentCategoryModel.objects.all()
    serializer_class = ComponentCategorySerializer


