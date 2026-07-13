from django.urls import include, path, re_path
from study import views
import fav.urls

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/create/$', views.create, name='study_create'),
    re_path(r'^(?P<pk>\d+)/$', views.detail, name='study_detail'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.edit, name='study_edit'),
    path('', include(fav.urls), {'app': 'study'}),
]
