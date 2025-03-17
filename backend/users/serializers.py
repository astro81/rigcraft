from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password') 
    
    def create(self, validated_data):
        """Override serializer create mathod to hash password via create_user() method
            Create a new user with the validated data and save it to the database.
            The password will automatically be hashed before being saved.
        Args:
            validated_data (_type_): _description_
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        
        return user