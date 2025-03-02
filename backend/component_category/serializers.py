from rest_framework import serializers
from component_category.models import ComponentCategoryModel

class ComponentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentCategoryModel
        fields = ('component_category_id',
                  'component_category_name',
                  'component_category_title',
                  'component_category_sub_title',
                  'component_category_description'
                )