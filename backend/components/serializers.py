from rest_framework import serializers
from components.models import ComponentCpuModel, ComponentMemoryModel, ComponentGpuModel

class ComponentCpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentCpuModel
        fields = (
			'component_cpu_id',
            'component_cpu_name',
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

class ComponentMemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentMemoryModel
        fields = (
			'component_memory_id',
   			'component_memory_name',
			'component_memory_producer',
			'component_memory_model',
			'component_memory_type',
			'component_memory_size',
			'component_memory_clock_speed',
			'component_memory_price',
			'component_memory_image'
		)

class ComponentGpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentGpuModel
        fields = (
            'component_gpu_id',
            'component_gpu_name',
            'component_gpu_brand',
            'component_gpu_model',
            'component_gpu_series',
            'component_gpu_vram',
            'component_gpu_boost_clock',
            'component_gpu_hdmi_port',
            'component_gpu_power_consumption',
            'component_gpu_price',
            'component_gpu_image'
        )