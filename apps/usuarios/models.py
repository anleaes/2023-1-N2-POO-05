from django.db import models

# Create your models here.


class User(models.Model):
    name_user = models.CharField('Nome de usuario', max_length=200)
    password = models.CharField('Senha', max_length=200)

    class meta:
        verbose_name = 'Nome'
        ordering = ['id']

    def __str__(self):
        return self.name
    
   