from django.shortcuts import render
from .models import Artista, Pessoa
from rest_framework import viewsets
from .serializer import ArtistaSerializer, PessoaSerializer

# Create your views here.

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer  


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer  