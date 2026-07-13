
from django.conf.urls import *
from userena import views as userena_views

from profiles.forms import BsEditProfileForm, BsSignupForm, SignupFormOnlyEmail

urlpatterns = patterns('',

                       url(r'^(?P<username>[\.\w]+)/edit/$',
                           userena_views.profile_edit,
                           {'edit_profile_form': BsEditProfileForm}, name='userena_profile_edit'),
                       url(r'^signup/$', userena_views.signup,
                           {'signup_form': BsSignupForm}, name='userena_signup'),

                       url(r'^', include('userena.urls')),
                       url(r'^(?P<username>[\.\w]+)/lmg/$', 'profiles.views.manager_lesson', name="le_mg"),
                       url(r'^email_confirm/(?P<c_key>\w+)/$', 'profiles.views.email_confirm', name="social_email_confirm"),
)
