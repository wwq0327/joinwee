from django.urls import re_path
from fav import views

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/fav/$', views.fav, name='fav'),
    re_path(r'^(?P<pk>\d+)/unfav/$', views.unfav, name='unfav'),
    re_path(r'^(?P<pk>\d+)/join/$', views.join, name='join'),
    re_path(r'^(?P<pk>\d+)/unjoin/$', views.unjoin, name='unjoin'),
]
