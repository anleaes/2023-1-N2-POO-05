from django.shortcuts import render
from .models import Album
from rest_framework import viewsets
from .serializer import AlbumSerializer

# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer  
    