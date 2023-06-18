from django.shortcuts import render

# Create your views here.
from .models import Comentario, Musica, Usuario
from rest_framework import viewsets
from .serializer import ComentarioSerializer, MusicaSerializer, UsuarioSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer  

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer 

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer   