from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('profiles.urls')),
    path('', include('home.urls')),
    path('lesson/', include('weelesson.urls')),
    path('meet/', include('weemeet.urls')),
    path('study/', include('study.urls')),
    path('discuss/', include('topics.urls')),
    path('blog/', include('blog.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
]

from hitcount.views import update_hit_count_ajax

urlpatterns += [
    path('ajax/hit/', update_hit_count_ajax, name='hitcount_update_ajax'),
]

urlpatterns += [
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=settings.MEDIA_URL + 'img/favicon.ico')),
]

from abugs.views import page_not_found, server_error, denied

handler404 = page_not_found
handler500 = server_error
handler403 = denied
