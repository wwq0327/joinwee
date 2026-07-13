from django.urls import path, re_path
from topics import views

urlpatterns = [
    path('', views.discuss_index, name='discuss_index'),
    re_path(r'^(?P<pk>\d+)/$', views.topic, name='t_topic'),
    re_path(r'^(?P<app>\w+)/(?P<pk>\d+)/create/$', views.create, name='t_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit, name='t_edit'),
    re_path(r'^(?P<pk>\d+)/del/$', views.delete, name='t_delete'),
    re_path(r'^comment/(?P<pk>\d+)/del/$', views.delete_comment, name='cm_del'),
]
