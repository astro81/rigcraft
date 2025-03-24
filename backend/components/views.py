from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from components.models import ComponentCpuModel, ComponentMemoryModel, ComponentGpuModel
from components.serializers import ComponentCpuSerializer, ComponentMemorySerializer, ComponentGpuSerializer

# Create your views here.
class ComponentBaseViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for components with common logic for retrieving objects by name or ID.
    """
    name_field = None  # Override this in child classes with the appropriate name field

    def get_object(self):
        # Get the `lookup_value` from the URL kwargs
        lookup_value = self.kwargs.get(self.lookup_field)

        # If the lookup value is a string (not a number), assume it's the `name`
        if lookup_value and not lookup_value.isdigit() and self.name_field:
            # Try to retrieve the object by the `name_field`
            obj = self.queryset.filter(**{self.name_field: lookup_value}).first()
            if obj:
                return obj
            else:
                # If no object is found, raise a 404 error
                raise NotFound(f"No component found with the given {self.name_field}.")

        # Fall back to the default behavior (retrieve by `id`)
        return super().get_object()



class ComponentCpuViewSet(ComponentBaseViewSet):
    queryset = ComponentCpuModel.objects.all()
    serializer_class = ComponentCpuSerializer
    name_field = 'component_cpu_name'               #* Use the name field for lookup

class ComponentMemoryViewSet(ComponentBaseViewSet):
    queryset = ComponentMemoryModel.objects.all()
    serializer_class = ComponentMemorySerializer
    name_field = 'component_memory_name'            #* Use the name field for lookup

class ComponentGpuViewSet(ComponentBaseViewSet):
    queryset = ComponentGpuModel.objects.all()
    serializer_class = ComponentGpuSerializer
    name_field = 'component_gpu_name'             #* Use the name field for lookup

