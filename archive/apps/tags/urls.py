from django.urls import re_path
from tags import views

urlpatterns = [
    re_path(r'^(?P<tag>[^/]+)/$', views.tag_item, name='tag_item'),
]
