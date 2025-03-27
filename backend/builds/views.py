from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from icecream import ic

from .models import BuildModel
from .serializers import BuildSerializer

class BuildViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling builds
    """
    serializer_class = BuildSerializer
    permission_classes = [AllowAny]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # ic(serializer)
        try:
            serializer.is_valid(raise_exception=True)
            build = serializer.save()
            
            ic(build)
            
            return Response({
                'message': 'Build saved successfully',
                'build': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'message': 'Failed to save build',
                'errors': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

