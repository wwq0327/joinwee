from django.urls import include, path, re_path
from weemeet import views
import fav.urls

urlpatterns = [
    path('', views.index, name='meet_index'),
    re_path(r'^(?P<pk>\d+)/$', views.detail, name='meet_detail'),
    re_path(r'^(?P<pk>\d+)/create/$', views.create, name='meet_create'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit, name='meet_edit'),
    re_path(r'^(?P<pk>\d+)/del/$', views.delete, name='meet_delete'),
    path('', include(fav.urls), {'app': 'weemeet'}),
]
