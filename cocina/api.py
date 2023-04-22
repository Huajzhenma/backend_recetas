from .models import Cocina
from rest_framework import viewsets, permissions
from .serializers import CocinaSerializer

class CocinaViewSet(viewsets.ModelViewSet):
    queryset = Cocina.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CocinaSerializer 