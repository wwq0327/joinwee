from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('succ/', views.succ, name='home_succ'),
    path('about/', views.about, name='home_about'),
]
