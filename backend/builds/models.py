from django.db import models
from django.contrib.auth.models import User
from components.models import ComponentCpuModel, ComponentMemoryModel, ComponentGpuModel

class BuildModel(models.Model):
    """
    Model to represent a user's computer build
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='builds')
    cpu = models.ForeignKey(ComponentCpuModel, on_delete=models.CASCADE)
    memory = models.ForeignKey(ComponentMemoryModel, on_delete=models.CASCADE)
    gpu = models.ForeignKey(ComponentGpuModel, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Computer Build"
        verbose_name_plural = "Computer Builds"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s Build - {self.created_at.strftime('%Y-%m-%d')}"

