from django.urls import include, path, re_path
from weelesson import views
from topics import views as topics_views
import fav.urls

urlpatterns = [
    path('', views.index, name='lesson_index'),
    re_path(r'^(?P<pk>\d+)/$', views.lesson, name='weelesson_detail'),
    path('create/', views.create, name='lesson_create'),
    re_path(r'^(?P<pk>\d+)/publish/info/$', views.info, name='lesson_info'),
    re_path(r'^(?P<pk>\d+)/publish/$', views.publish, name='lesson_publish'),
    re_path(r'^(?P<pk>\d+)/unpublish/$', views.unpublish, name='lesson_unpublish'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit, name='lesson_edit'),
    re_path(r'^(?P<pk>\d+)/del/$', views.delete, name='lesson_delete'),
    path('', include(fav.urls), {'app': 'weelesson'}),
    re_path(r'^(?P<pk>\d+)/draft/$', views.draft, name='lesson_draft'),
    re_path(r'^(?P<pk>\d+)/discuss/$', topics_views.all, name='t_all'),
]
