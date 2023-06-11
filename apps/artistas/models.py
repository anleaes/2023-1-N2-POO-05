from django.db import models

# Create your models here.

class Artista(models.Model):
    name = models.CharField('Nome', max_length=50)

    STATUS_CHOICES = (
        ('Vocalista', 'Vocalista'),
        ('Baterista', 'Baterista'),
        ('Guitarrista', 'Guitarrista'),
        ('Tecladista', 'Tecladista'),
        ('Violinista', 'Violinista'),
    )
    status = models.CharField('Status', max_length=12, choices=STATUS_CHOICES, null=True, blank=True, default='Vocalista')
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name