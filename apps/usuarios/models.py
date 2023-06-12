from django.db import models
from pessoas.models import Pessoa

# Create your models here.


class User(models.Model):
    name_user = models.CharField('Nome de usuario', max_length=200)
    password = models.CharField('Senha', max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)

    class meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

    def __str__(self):
        return self.name_user
    

            
