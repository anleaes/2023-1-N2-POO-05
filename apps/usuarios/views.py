from django.shortcuts import render

# Create your views here.
from .models import Usuario, Pessoa
from rest_framework import viewsets
from .serializer import UsuarioSerializer, PessoaSerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer  