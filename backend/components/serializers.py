from rest_framework import serializers
from components.models import ComponentCpuModel

class ComponentCpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentCpuModel
        fields = ('component_cpu_id',
                  'component_cpu_name',
                  'component_cpu_brand',
                  'component_cpu_brand',
                  'component_cpu_series',
                  'component_cpu_model',
                  'component_cpu_socket',
                  'component_cpu_clock_speed',
                  'component_cpu_cores',
                  'component_cpu_threads',
                  'component_cpu_price',
                  'component_cpu_image'
                )