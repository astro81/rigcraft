from rest_framework import serializers
from .models import BuildModel
from components.serializers import ComponentCpuSerializer, ComponentMemorySerializer, ComponentGpuSerializer
from components.models import ComponentCpuModel, ComponentMemoryModel, ComponentGpuModel


class BuildSerializer(serializers.ModelSerializer):
    cpu = ComponentCpuSerializer(read_only=True)
    memory = ComponentMemorySerializer(read_only=True)
    gpu = ComponentGpuSerializer(read_only=True)
    
    cpu_id = serializers.PrimaryKeyRelatedField(
        queryset=ComponentCpuModel.objects.all(), 
        write_only=True
    )
    memory_id = serializers.PrimaryKeyRelatedField(
        queryset=ComponentMemoryModel.objects.all(), 
        write_only=True
    )
    gpu_id = serializers.PrimaryKeyRelatedField(
        queryset=ComponentGpuModel.objects.all(), 
        write_only=True
    )
    
    class Meta:
        model = BuildModel
        fields = ['id', 'cpu', 'memory', 'gpu', 'cpu_id', 'memory_id', 'gpu_id', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def create(self, validated_data):
        """
        Create a new build for the authenticated user
        """
        user = self.context['request'].user
        
        validated_data['user'] = user
        validated_data['cpu'] = validated_data.pop('cpu_id')
        validated_data['memory'] = validated_data.pop('memory_id')
        validated_data['gpu'] = validated_data.pop('gpu_id')
        
        return super().create(validated_data)

