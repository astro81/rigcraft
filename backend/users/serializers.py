from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from typing import Dict, Any
from .models import UserProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=4,
        max_length=128,
    )
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'profile_picture', 'bio')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }
    
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check for empty fields
        if not username:
            raise serializers.ValidationError({"username": "Username is required."})
        if not email:
            raise serializers.ValidationError({"email": "Email is required."})
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})

        #* Check if username already exists
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "A user with that username already exists."})

        #* Check if email already exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "A user with that email already exists."})

        return data
    
    def create(self, validated_data: Dict[str, Any]) -> User:
        """
        *Create user with profile information.
        
        Args:
            validated_data: Validated data containing user and profile fields.
        
        Returns:
            User: The newly created user instance.
        """
        
        #* Extract profile fields
        profile_picture = validated_data.pop('profile_picture', None)
        bio = validated_data.pop('bio', None)
        
        #* Create user with core fields
        user = User.objects.create_user(
            **{k: v for k, v in validated_data.items() if k != 'password'},
            password=validated_data['password']
        )
        
        #* Update profile information
        profile, created = UserProfile.objects.get_or_create(user=user)

        if profile_picture or bio:
            profile = UserProfile.objects.get(user=user)
            if profile_picture:
                profile.profile_picture = profile_picture
            if bio:
                profile.bio = bio
            profile.save()
        
        return user
    
    def to_representation(self, instance):
        """
        *Customize the output representation after creation
        """
        data = super().to_representation(instance)
        data['message'] = 'User registered successfully'
        return data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        #* Check for empty fields
        if not username:
            raise serializers.ValidationError({"username": "Username is required."})
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})
        
        #* Authenticate the user
        user = authenticate(username=username, password=password)
        
        if not user:
            #* Check if the user exists
            if not User.objects.filter(username=username).exists():
                raise serializers.ValidationError({"username": "No user found with that username."})
            else:
                raise serializers.ValidationError({"password": "Incorrect password."})

        #! Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    
    profile_picture = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio']
    
    def validate_username(self, value):
        # Get the current user
        user = self.instance.user if self.instance else None
        
        # Check if the username is already taken by another user
        if User.objects.exclude(pk=user.pk if user else None).filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value    
    
    def validate_email(self, value):
        # Get the current user
        user = self.instance.user if self.instance else None
        
        # Check if the email is already used by another user
        if User.objects.exclude(pk=user.pk if user else None).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
    
    def update(self, instance, validated_data):
        # Extract user data
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        # Update user fields (including username and email now)
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()
        
        # Update profile fields
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        
        return instance
    


class AccountDeletionSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        password = data.get('password')
        user = self.context.get('user')

        # Check for empty password
        if not password:
            raise serializers.ValidationError({"password": "Password is required."})
        
        # Verify the password
        if not user.check_password(password):
            raise serializers.ValidationError({"password": "Incorrect password."})

        return data

