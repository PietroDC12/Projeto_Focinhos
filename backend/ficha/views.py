from rest_framework import generics, permissions

from .models import Ficha
from .serializers import FichaSerializer

class FichaList(generics.ListAPIView):
    """Listando ficha"""
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    permission_classes = ()

class FichaDestroy(generics.DestroyAPIView):
    """Excluindo ficha"""
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class FichaUpdate(generics.UpdateAPIView):
    """Update de ficha"""
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class FichaCreate(generics.CreateAPIView):
    """Criando ficha"""
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class FichaGet(generics.RetrieveAPIView):
    """Listando uma ficha"""
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer
    permission_classes = ()

