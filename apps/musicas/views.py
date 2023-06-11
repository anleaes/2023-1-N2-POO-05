from django.shortcuts import render
from .models import Musica
from rest_framework import viewsets
from .serializer import MusicaSerializer

# Create your views here.

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer  