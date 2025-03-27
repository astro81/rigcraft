# users/views.py
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import (
    UserRegistrationSerializer, 
    UserLoginSerializer, 
    UserProfileSerializer, 
    AccountDeletionSerializer
)

import os
import shutil
import logging

logger = logging.getLogger(__name__)

class RegistrationAPIView(CreateAPIView):
    """
    *API view for user registration with comprehensive handling.
    
    Allows user registration with profile information and token generation.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        *Handle user registration process.
        
        Args:
            request: Incoming HTTP request
        
        Returns:
            Response: Registration response with tokens and user data
        """
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
                        
            return Response({
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            logger.error(f"Registration Error: {str(e)}")
            return Response({
                'message': 'Registration failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    """
    *API view for user login with secure token generation.
    """
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        """
        *Handle user login process.
        
        Args:
            request: Incoming HTTP request
        
        Returns:
            Response: Login response with tokens
        """
        serializer = self.serializer_class(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            
            return Response({
                'message': 'Login successful',
                'access_token': serializer.validated_data['access'],
                'refresh_token': serializer.validated_data['refresh'],
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(f"Login Error: {str(e)}")
            return Response({
                'message': 'Login failed',
                'errors': serializer.errors
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    *API view for retrieving and updating user profiles.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        *Retrieve or create user profile.
        
        Returns:
            UserProfile: User's profile instance
        """
        try:
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            return UserProfile.objects.create(user=self.request.user)


class AccountDeletionAPIView(APIView):
    """
    *API view for secure account deletion.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """
        *Handle account deletion process.
        
        Args:
            request: Incoming HTTP request
        
        Returns:
            Response: Account deletion status
        """
        serializer = AccountDeletionSerializer(
            data=request.data, 
            context={'user': request.user}
        )
        
        if serializer.is_valid():
            user = request.user
            
            try:
                profile = user.profile
                
                # Delete profile picture safely
                if (profile.profile_picture) and ('default_profile.png' not in profile.profile_picture.name):
                    self._delete_profile_picture(profile)
                
                # Delete user account
                user.delete()
                
                return Response({
                    'message': 'Account deleted successfully'
                }, status=status.HTTP_200_OK)
                
            except Exception as e:
                logger.error(f"Account Deletion Error: {str(e)}")
                return Response({
                    'message': 'Failed to delete account',
                    'error': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response({
            'message': 'Account deletion failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def _delete_profile_picture(self, profile):
        """
        *Safely delete user's profile picture.
        
        Args:
            profile (UserProfile): User profile instance
        """
        try:
            picture_path = profile.profile_picture.path
            user_dir = os.path.dirname(picture_path)
            
            if os.path.exists(picture_path):
                os.remove(picture_path)
            
            if os.path.exists(user_dir) and os.path.basename(user_dir).startswith('user_'):
                shutil.rmtree(user_dir)
        
        except Exception as e:
            logger.warning(f"Profile picture deletion error: {str(e)}")


class UserLogoutAPIView(APIView):
    """
    *API view for user logout with secure token handling.
    
    Handles user logout by blacklisting the refresh token.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        """
        *Handle user logout process.
        
        Expects a refresh token in the request body.
        Blacklists the refresh token to invalidate the user's session.
        
        Args:
            request: Incoming HTTP request with refresh token
        
        Returns:
            Response: Logout status
        """
        try:
            # Get refresh token from request
            refresh_token = request.data.get('refresh_token')
            
            # Validate refresh token presence
            if not refresh_token:
                return Response({
                    'message': 'Refresh token is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                # Attempt to blacklist the token
                token = RefreshToken(refresh_token)
                token.blacklist()
                
                return Response({
                    'message': 'Logout successful'
                }, status=status.HTTP_200_OK)
            
            except TokenError:
                # Handle invalid token scenarios
                return Response({
                    'message': 'Invalid or expired token'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Log unexpected errors
            logger.error(f"Logout Error: {str(e)}")
            return Response({
                'message': 'Logout failed',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

