from django.db import models
from pessoas.models import Pessoa

# Create your models here.

class Artista(models.Model):
    STATUS_CHOICES = (
        ('Vocalista', 'Vocalista'),
        ('Baterista', 'Baterista'),
        ('Guitarrista', 'Guitarrista'),
        ('Tecladista', 'Tecladista'),
        ('Violinista', 'Violinista'),
    )
    funcao = models.CharField('Função', max_length=12, choices=STATUS_CHOICES, null=True, blank=True, default='Vocalista')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name
