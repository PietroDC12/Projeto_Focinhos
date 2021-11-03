from rest_framework import serializers
from .models import BuscaImagem

class BuscaImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuscaImagem
        fields = (
            '__all__')