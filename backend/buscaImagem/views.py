from rest_framework import generics, permissions

from .models import BuscaImagem
from .serializers import BuscaImagemSerializer

class BuscaImagemList(generics.ListAPIView):
    
    queryset = BuscaImagem.objects.all()
    serializer_class = BuscaImagemSerializer
    permission_classes = ()

class BuscaImagemDestroy(generics.DestroyAPIView):
    
    queryset = BuscaImagem.objects.all()
    serializer_class = BuscaImagemSerializer


class BuscaImagemUpdate(generics.UpdateAPIView):
    
    queryset = BuscaImagem.objects.all()
    serializer_class = BuscaImagemSerializer

class BuscaImagemCreate(generics.CreateAPIView):
   
    queryset = BuscaImagem.objects.all()
    serializer_class = BuscaImagemSerializer

class BuscaImagemGet(generics.RetrieveAPIView):
    
    queryset = BuscaImagem.objects.all()
    serializer_class = BuscaImagemSerializer
    permission_classes = ()

