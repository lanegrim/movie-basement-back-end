from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
