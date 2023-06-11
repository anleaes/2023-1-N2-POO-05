from django.db import models
from albums.models import Album
from artistas.models import Artista
# Create your models here.

class Musica(models.Model):
    name = models.CharField('Nome', max_length=50)
    genero = models.CharField('Genero', max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musica'
        ordering =['id']

    def __str__(self):
        return self.name
    
#client = models.ForeignKey(Client, on_delete=models.CASCADE)
#from socialnetworks.models import Socialnetwork