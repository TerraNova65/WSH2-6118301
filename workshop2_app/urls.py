from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_detail/', views.movie_detail, name='movie_detail'),
    path('', views.homepage, name='homepage'),
]