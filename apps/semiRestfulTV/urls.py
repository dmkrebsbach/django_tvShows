from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.showAll),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.createShow),
    url(r'^shows/(?P<showId>\d+)$', views.showDesc),
    url(r'^shows/(?P<showId>\d+)/edit$', views.editShow),
    url(r'^shows/(?P<showId>\d+)/update$', views.updateShow),
    url(r'^shows/(?P<showId>\d+)/destroy$', views.destroyShow),
]