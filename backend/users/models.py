from django.db import models
from django.contrib.auth.models import User
import os

def default_profile_picture():
    #* Path to the default profile picture
    return 'users/profile_pictures/default_profile.png'

def user_profile_picture_path(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]
    
    # Create a unique filename
    filename = f"profile_picture.{ext}"
    
    # Return the complete path with user-specific directory
    return os.path.join('users/profile_pictures', f"user_{instance.user.username}", filename)

class UserProfile(models.Model):
    """
    *Extended user profile model.

    *This model extends the default Django User model with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to=user_profile_picture_path, 
        default=default_profile_picture, 
        null=True, 
        blank=True
    )
    bio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
