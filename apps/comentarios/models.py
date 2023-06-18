from django.db import models
from musicas.models import Musica
from usuarios.models import Usuario
# from Musicas.models import Musica

# Create your models here.
class Comentario(models.Model):
    description = models.TextField('Comentario', max_length=100)
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering =['id']

    def __str__(self):
        return self.description