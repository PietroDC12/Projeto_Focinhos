from rest_framework import generics, permissions

from cadastro.models import Info
from cadastro.serializers import InfoSerializer

class InfoList(generics.ListAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = ()

class InfoDestroy(generics.DestroyAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )

class InfoUpdate(generics.UpdateAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (
        permissions.IsAuthenticated, #talvez deixar só pro admin
    )

class InfoCreate(generics.CreateAPIView):
   
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )

class InfoGet(generics.RetrieveAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = ()
