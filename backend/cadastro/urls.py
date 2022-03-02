from django.conf.urls import url

from .views import (InfoList, InfoDestroy, InfoCreate, InfoGet, InfoUpdate)

urlpatterns = [
    url(r'info/$', InfoList.as_view()),
    url(r'info(?P<pk>\d+)/$', InfoDestroy.as_view()),
    url(r'info/add/$', InfoCreate.as_view()),
    url(r'info/get/(?P<pk>\d+)/$', InfoGet.as_view()),
    url(r'info/edit/(?P<pk>\d+)/$', InfoUpdate.as_view()),
]