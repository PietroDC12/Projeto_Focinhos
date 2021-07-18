from django.conf.urls import url

from .views import (
    InfoList, InfoDestroy, InfoCreate, InfoGet, InfoUpdate
)

urlpatterns = [
    url(r'cadastro/$', InfoList.as_view()),
    url(r'cadastro(?P<pk>\d+)/$', InfoDestroy.as_view()),
    url(r'cadastro/add/$', InfoCreate.as_view()),
    url(r'cadastro/get/(?P<pk>\d+)/$', InfoGet.as_view()),
    url(r'cadastro/edit/(?P<pk>\d+)/$', InfoUpdate.as_view()),
]