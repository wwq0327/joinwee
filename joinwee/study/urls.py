from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/create/$', 'study.views.create', name="study_create"),
                       url(r'^(?P<pk>\d+)/$', 'study.views.detail', name="study_detail"),
                       url(r'^(?P<pk>\d+)/edit/$', 'study.views.edit', name="study_edit"),
                       url(r'^', include('fav.urls'), {'app': 'study'}),
)                       
