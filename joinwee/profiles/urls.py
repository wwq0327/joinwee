from django.urls import path, re_path
from profiles import views

urlpatterns = [
    path('profile_list/', views.profile_list, name='profile_list'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.profile_detail, name='profile_detail'),
    re_path(r'^(?P<username>[\w.@+-]+)/edit/$', views.profile_edit, name='userena_profile_edit'),
    re_path(r'^(?P<username>[\w.@+-]+)/lmg/$', views.manager_lesson, name='le_mg'),
    path('email_confirm/<c_key>/', views.email_confirm, name='social_email_confirm'),
]
