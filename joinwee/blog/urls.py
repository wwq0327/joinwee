from django.conf.urls import *

urlpatterns = patterns('',
                       url('^$', 'blog.views.index', name="blog_index"),
                       url('^p/(?P<slug>[^\.]+)/$', 'blog.views.post', name="blog_post"),
)                       
