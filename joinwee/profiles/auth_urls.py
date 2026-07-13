from django.urls import path, re_path
from profiles import views

urlpatterns = [
    path('new-social-user/', views.new_social_user, name='new_social'),
    path('sns-link/', views.sns_link, name='sns_link'),
    path('sns-redirect/', views.sns_redirect, name='sns_redirect'),
]
