from django.shortcuts import render
from .models import Artistas
from rest_framework import viewsets
from .serializer import ArtistasSerializer

# Create your views here.
class ArtistasViewSet(viewsets.ModelViewSet):
    queryset = Artistas.objects.all()
    serializer_class = ArtistasSerializer  