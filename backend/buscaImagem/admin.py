from django.contrib import admin
from .models import BuscaImagem

class ImagensBusca(admin.ModelAdmin):
    list_display = ('imagem_busca')
    list_display_links = ('imagem_busca')
    search_fields = ('imagem_busca')
    list_per_page = 10

admin.site.register(BuscaImagem, ImagensBusca)