from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

import notifications

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('profiles.urls')),
    url('^', include('home.urls')),
    url(r'^lesson/', include('weelesson.urls')),
    url(r'^meet/', include('weemeet.urls')),
    url(r'^study/', include('study.urls')),
    url(r'^discuss/', include('topics.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^notifications/', include(notifications.urls)),
#    url(r'^tag/', include('tags.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^oauth/', include('profiles.auth_urls')),
)

#hitcount
from hitcount.views import update_hit_count_ajax

urlpatterns += patterns('',
                        url(r'^ajax/hit/$',
                            update_hit_count_ajax,
                            name='hitcount_update_ajax'),
)

# robots.txt

from django.views.generic import TemplateView

urlpatterns += patterns('',
        url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)            

media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                }),
)

from django.views.generic import RedirectView

urlpatterns += patterns('',
    (r'^favicon\.ico$', RedirectView.as_view(url=settings.MEDIA_URL + 'img/favicon.ico'))
)

handler404 = 'abugs.views.page_not_found'
handler500 = 'abugs.views.server_error'
handler403 = 'abugs.views.denied'
