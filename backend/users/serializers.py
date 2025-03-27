# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Dict, Any
from .models import UserProfile
from icecream import ic

class BaseUserValidationMixin:
    """
    *Mixin for common user validation logic.
    
    Provides shared validation methods across serializers.
    """
    def validate_username(self, value):
        """
        *Validate username uniqueness and format.
        
        Args:
            value (str): Username to validate
        
        Returns:
            str: Validated username
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        return value

    def validate_email(self, value):
        """
        *Validate email uniqueness and format.
        
        Args:
            value (str): Email to validate
        
        Returns:
            str: Validated email
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use.")
        return value

    def validate_password(self, value):
        """
        *Advanced password validation.
        
        Args:
            value (str): Password to validate
        
        Returns:
            str: Validated password
        """
        # todo: uncoment the validation method
        # validate_password(value)
        #! Remove the manual method 
        if len(value) < 4:
            raise serializers.ValidationError("Password must be at least 4 characters long.")
        return value

class UserRegistrationSerializer(BaseUserValidationMixin, serializers.ModelSerializer):
    """
    *Serializer for user registration with comprehensive validation.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 
            'email', 'password', 'profile_picture', 'bio'
        ]
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }
    
    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        *Create user with associated profile.
        
        Args:
            validated_data (dict): Validated registration data
        
        Returns:
            User: Newly created user instance
        """
        profile_picture = validated_data.pop('profile_picture', None)
        bio = validated_data.pop('bio', None)
        
        user = User.objects.create_user(
            **{k: v for k, v in validated_data.items() if k != 'password'},
            password=validated_data['password']
        )
        
        profile, _ = UserProfile.objects.get_or_create(user=user)
        
        if profile_picture:
            profile.profile_picture = profile_picture
        if bio:
            profile.bio = bio
        
        profile.save()
        
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    *Serializer for user login with token generation.
    """
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True, 
        style={'input_type': 'password'}
    )
    
    def validate(self, data):
        """
        *Validate user credentials and generate tokens.
        
        Args:
            data (dict): Login credentials
        
        Returns:
            dict: Validated data with tokens
        """
        username = data.get('username')
        password = data.get('password')

        if not username:
            raise serializers.ValidationError({"username": "Username is required."})
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})
        
        user = authenticate(username=username, password=password)
        
        # if not user:
        #     raise serializers.ValidationError("Invalid login credentials.")
        
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "No user found with that username."})
        
        
        refresh = RefreshToken.for_user(user)
        
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        ic(data)
        
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    """
    *Comprehensive user profile serializer.
    """
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio']


    def update(self, instance, validated_data):
        """
        *Update user and profile data.
        
        Args:
            instance (UserProfile): Current profile instance
            validated_data (dict): Validated update data
        
        Returns:
            UserProfile: Updated profile instance
        """
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance


class AccountDeletionSerializer(serializers.Serializer):
    """
    *Serializer for secure account deletion.
    """
    password = serializers.CharField(
        write_only=True, 
        required=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, data):
        """
        *Validate deletion request.
        
        Args:
            data (dict): Deletion request data
        
        Returns:
            dict: Validated data
        """
        user = self.context.get('user')
        password = data.get('password')
        
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})
        
        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Incorrect password."})
        
        return data
    
