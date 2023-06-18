from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField('Nome', max_length=50)
    ano_de_lancamento = models.TextField('Ano de lancamento', max_length=30)
    tempo_de_duracao = models.TextField('Tempo de duracao', max_length=30)
    
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering =['id']

    def __str__(self):
        return self.name