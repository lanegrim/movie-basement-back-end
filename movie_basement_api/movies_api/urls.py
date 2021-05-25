from django.urls import path
from . import views

urlpatterns = [
    path('api/movies', views.MovieList.as_view(), name='movie_list'),
    path('api/movies/<int:pk>',
         views.MovieDetail.as_view(), name='movie_detail'),
]
