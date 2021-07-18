from django.contrib import admin
from .models import Info

class Infos(admin.ModelAdmin):
    list_display = ('cachorro_id', 'nome_cachorro')
    list_display_links = ('cachorro_id', 'nome_cachorro')
    search_fields = ('cachorro_id',)
    list_per_page = 10

admin.site.register(Info, Infos)