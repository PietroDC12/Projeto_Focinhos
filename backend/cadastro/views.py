from rest_framework import generics, permissions

from .models import Info
from .serializers import InfoSerializer

class InfoList(generics.ListAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = ()

class InfoDestroy(generics.DestroyAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoUpdate(generics.UpdateAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoCreate(generics.CreateAPIView):
   
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoGet(generics.RetrieveAPIView):
    
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = ()
