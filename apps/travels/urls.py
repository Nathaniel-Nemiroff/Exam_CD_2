from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^destination/(?P<id>\d+)$', views.destination, name='dest'),
	url(r'^add$', views.add, name='add'),
	url(r'^create_trip', views.create_trip, name='create_trip'),
	url(r'^join/(?P<id>\d+)$', views.join, name='join')
]
