from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^p/(?P<slug>[^\.]+)/$', views.post, name='blog_post'),
]
