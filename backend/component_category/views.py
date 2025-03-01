from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from component_category.models import ComponentCategoryModel
from component_category.serializers import ComponentCategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ComponentCategoryModel.objects.all()
    serializer_class = ComponentCategorySerializer

    def get_object(self):
        # Get the `lookup_field` from the URL kwargs
        lookup_value = self.kwargs.get(self.lookup_field)

        # If the lookup value is a string (not a number), assume it's the `component_category_name`
        if lookup_value and not lookup_value.isdigit():
            # Try to retrieve the object by `component_category_name`
            obj = self.queryset.filter(component_category_name=lookup_value).first()
            if obj:
                return obj
            else:
                # If no object is found, raise a 404 error
                from rest_framework.exceptions import NotFound
                raise NotFound("No component category found with the given name.")

        # Fall back to the default behavior (retrieve by `id`)
        return super().get_object()