from django.db import models

# Create your models here.

class Musica(models.Model):
    name = models.CharField('Nome', max_length=50)
    
    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musica'
        ordering =['id']

    def __str__(self):
        return self.name