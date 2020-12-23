from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Usuario(models.Model):
    class TipoDeUsuario(models.TextChoices):
        OPERADOR = 'OP', _('Operador')
        GERENTE = 'GER', _('Gerente')

    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=15)
    tipo = models.CharField(
        max_length=2,
        choices=TipoDeUsuario.choices,
        default=TipoDeUsuario.OPERADOR,
    )
    senha = models.CharField(max_length=20)

"""
class Estante(models.Model):

class Categoria(models.Model):

class Produto(models.Model):

class Remessa(models.Model):"""