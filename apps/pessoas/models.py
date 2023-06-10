from django.db import models

# Create your models here.

class Pessoa(models.Model):
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', max_length=50)
    idade = models.CharField('Idade', max_length=2)
    email = models.CharField('Email', max_length=50)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return self.name