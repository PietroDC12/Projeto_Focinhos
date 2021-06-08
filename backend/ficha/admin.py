from django.contrib import admin
from .models import Ficha

class Fichas(admin.ModelAdmin):
    list_display = ('nome_cachorro',)
    list_display_links = ('nome_cachorro',)
    list_per_page = 5

admin.site.register(Ficha, Fichas)