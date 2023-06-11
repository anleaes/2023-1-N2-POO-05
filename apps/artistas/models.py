from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Artista(models.Model):
    # name = models.CharField('Nome', max_length=50)
    # description = models.TextField('Descricao', max_length=100)
    EQUIPMENT_CHOICES = (
    ('Vocalista', 'Vocalista'),
    ('Baterista', 'Baterista'),
    ('Guitarrista', 'Guitarrista'),
    ('Baixista', 'Baixista'),
    ('Tecladista', 'Tecladista'),
)

    pessoas = models.ManyToManyField(Pessoa, blank=True)
    equipment = models.CharField('Função', max_length=11, default='Vocalista', choices=EQUIPMENT_CHOICES)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name
    #############################################

    ##############################################
    # class ClientPessoa(models.Model):
    #     # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #     Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        

    #     # artista_Pessoa = models.ManyToManyField(Pessoa, through='ClientSocialnetwork', blank=True)
    # class Meta:
    #     verbose_name = 'Item de Redes Social'
    #     verbose_name_plural = 'Itens de Rede Social'
    #     ordering =['id']

    # def __str__(self):
    #     return self.Pessoa.name 

    