from django.conf.urls import url

from .views import (
    FichaList, FichaDestroy, FichaCreate, FichaGet, FichaUpdate
)

urlpatterns = [
    url(r'fichas/$', FichaList.as_view()),
    url(r'fichas/(?P<pk>\d+)/$', FichaDestroy.as_view()),
    url(r'fichas/add/$', FichaCreate.as_view()),
    url(r'fichas/get/(?P<pk>\d+)/$',FichaGet.as_view()),
    url(r'fichas/edit/(?P<pk>\d+)/$', FichaUpdate.as_view()),
]