from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BuildModel
from .serializers import BuildSerializer

class BuildViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling build-related operations
    """
    serializer_class = BuildSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return builds only for the current user
        """
        return BuildModel.objects.filter(user=self.request.user)
    