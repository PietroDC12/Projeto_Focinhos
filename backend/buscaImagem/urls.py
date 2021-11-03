from django.conf.urls import url

from .views import (BuscaImagemList, BuscaImagemDestroy, BuscaImagemCreate, BuscaImagemGet, BuscaImagemUpdate)

urlpatterns = [
    url(r'busca_imagem/$', BuscaImagemList.as_view()),
    url(r'busca_imagem(?P<pk>\d+)/$', BuscaImagemDestroy.as_view()),
    url(r'busca_imagem/add/$', BuscaImagemCreate.as_view()),
    url(r'busca_imagem/get/(?P<pk>\d+)/$', BuscaImagemGet.as_view()),
    url(r'busca_imagem/edit/(?P<pk>\d+)/$', BuscaImagemUpdate.as_view()),
]