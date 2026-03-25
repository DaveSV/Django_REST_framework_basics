
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from quickstart.serializers import UserSerializer, GroupSerializer
from .models import Proyecto
from .serializers import ProyectoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    # Cambiamos la regla solo para esta vista:
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]