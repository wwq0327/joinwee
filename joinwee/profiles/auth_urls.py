from django.conf.urls import *

urlpatterns = patterns('',
                       url(r'^new-social-user/$', 'profiles.views.new_social_user', name="new_social"),
                       url(r'^sns-link/$', 'profiles.views.sns_link', name="sns_link"),
                       url(r'^sns-redirect/$', 'profiles.views.sns_redirect', name="sns_redirect"),
 
)
