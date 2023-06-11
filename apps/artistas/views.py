from django.shortcuts import render
from .models import Artista
from rest_framework import viewsets
from .serializer import ArtistaSerializer
# Create your views here.

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer  