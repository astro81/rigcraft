from rest_framework import serializers
from .models import BuildModel

class BuildSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving builds
    """
    class Meta:
        model = BuildModel
        fields = ['id', 'cpu', 'memory', 'gpu', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Override create method to set the current user
        """
        user = self.context.get('request').user
        validated_data['user'] = user
        return super().create(validated_data)

