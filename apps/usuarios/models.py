from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    senha = models.CharField('Senha', max_length=50)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.nome
    
    #onetoone