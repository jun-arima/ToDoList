from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<task_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<task_id>[0-9]+)/update/$', views.update, name='update'),
    url(r'^create/$', views.create, name='create'),
]
