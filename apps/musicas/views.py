from django.shortcuts import render
from .models import Musica, Album, Artista
from rest_framework import viewsets
from .serializer import MusicaSerializer, AlbumSerializer, ArtistaSerializer

# Create your views here.

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer  

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer  

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer  