from users.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import UserProfile
from users.serializers import UserRegistrationSerializer, AccountDeletionSerializer
import os, shutil
from icecream import ic

class RegistrationAPIView(CreateAPIView):
    """
    *API view for user registration with profile information.
    
    *This view allows any user to register by providing username, password, and optional
    *profile information like first name, last name, email, profile picture, and bio.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        #* Generate tokens after successful registration
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'User registered successfully',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)

class UserLoginAPIView(APIView):
    """
    *API view for user login.
    
    *This view authenticates the user and returns JWT tokens if the credentials are valid.
    """
    serializer_class = UserLoginSerializer
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            #* fetch the access token and refresh token from the serializer
            access_token: str =  serializer.validated_data['access']
            refresh_token: str = serializer.validated_data['refresh']
            
            return Response({
                'message': 'Login successful',
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Invalid credentials',
                'errors': serializer.errors,
            }, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutAPIView(APIView):
    """
    *API view for user logout.
    
    *This view blacklists the refresh token to log out the user.
    """
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            
            ic(refresh_token)
            
            if not refresh_token:
                return Response({
                    'message': 'Refresh token is required.',
                }, status=status.HTTP_400_BAD_REQUEST)

            try:
                token = RefreshToken(refresh_token)

                token.blacklist()

                return Response({
                    'message': 'Logout successful',
                }, status=status.HTTP_200_OK)
            except Exception as token_error:
                return Response({
                    'message': 'Token processing error',
                    'error': str(token_error)
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # General error handler
            return Response({
                'message': 'Invalid token',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    *API view for retrieving and updating the authenticated user's profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  #! Only authenticated users can access this view

    def get_object(self):
        try:
            #* Return the UserProfile instance for the authenticated user
            return self.request.user.profile
        except UserProfile.DoesNotExist:
            #* If the profile does not exist, create it
            return UserProfile.objects.create(user=self.request.user)


class AccountDeletionAPIView(APIView):
    """
    *API view for user account deletion.
    
    *This view deletes the user account after password verification.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = AccountDeletionSerializer(data=request.data, context={'user': request.user})
        
        if serializer.is_valid():
            user = request.user
            
            try:
                # Get the profile to access file paths
                profile = user.profile
                
                # Delete profile picture if it exists and isn't the default
                if profile.profile_picture and not profile.profile_picture.name.endswith('default_profile.png'):
                    # Get the directory path
                    user_dir = os.path.dirname(profile.profile_picture.path)
                    
                    # Delete the file
                    if os.path.exists(profile.profile_picture.path):
                        os.remove(profile.profile_picture.path)
                    
                    # Delete the user directory if it exists
                    if os.path.exists(user_dir) and os.path.basename(user_dir).startswith('user_'):
                        shutil.rmtree(user_dir)
                
                # Delete the user (this will cascade to the profile as well)
                user.delete()
                
                return Response({
                    'message': 'Account deleted successfully'
                }, status=status.HTTP_200_OK)
                
            except Exception as e:
                return Response({
                    'message': 'Failed to delete account',
                    'error': str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({
                'message': 'Failed to delete account',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)