from django.conf.urls import url
from . import views
from django.contrib.auth import views as aviews

urlpatterns = [
    url(r'^login/$', aviews.login, name='login'),
    url(r'^logout/$', aviews.logout, name='logout'),
]
