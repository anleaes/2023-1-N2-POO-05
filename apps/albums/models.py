from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering =['id']

    def __str__(self):
        return self.name