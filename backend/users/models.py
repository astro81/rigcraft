# users.models
from django.db import models
from django.contrib.auth.models import User
import os
import uuid


# def default_profile_picture():
#     #* Path to the default profile picture
#     return 'users/profile_pictures/default_profile.png'

def default_profile_picture():
    """
    *Provides the default profile picture path.
    
    Returns:
        str: Path to the default profile picture
    """
    return 'users/profile_pictures/default_profile.png'

def generate_unique_filename(instance, filename):
    """
    *Generate a unique filename for uploaded files.
    
    Args:
        instance: Model instance
        filename: Original filename
    
    Returns:
        str: Unique filepath for the uploaded file
    """
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('users/profile_pictures', 
                        f"user_{instance.user.username}", 
                        unique_filename)


class UserProfile(models.Model):
    """
    *Extended user profile model.

    *Provides additional user information beyond the default Django User model.
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )

    profile_picture = models.ImageField(
        upload_to=generate_unique_filename,
        default=default_profile_picture,
        null=True,
        blank=True
    )
    
    
    bio = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_full_name(self):
        """
        *Return the user's full name.
        
        Returns:
            str: Formatted full name
        """
        return f"{self.user.first_name} {self.user.last_name}".strip()
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        
