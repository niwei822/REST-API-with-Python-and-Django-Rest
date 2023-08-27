from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from myapp.models import Movie
from .serializers import MovieSerializer


class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer