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
        max_length=3,
        choices=TipoDeUsuario.choices,
        default=TipoDeUsuario.OPERADOR,
    )
    senha = models.CharField(max_length=20)


class Estante(models.Model):
    codigo = models.CharField(max_length=50)
    galpao = models.CharField(max_length=50)
    corredor = models.CharField(max_length=50)
    quantidade_prateleiras = models.IntegerField(blank=True, null=True)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)


class Produto(models.Model):
    id_categoria = models.ForeignKey(Categoria,
                                     default=00,
                                     on_delete=models.SET_DEFAULT,
                                     verbose_name='ID Categoria')
    qr_code_url = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    largura = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    comprimento = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    descricao = models.CharField(max_length=350)
    num_prateleira = models.IntegerField(default=0)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    valor_venda = models.DecimalField(max_digits=12, decimal_places=2, default=15.00)
    id_estante = models.ForeignKey(Estante,
                                   on_delete=models.CASCADE,
                                   verbose_name='ID Estante')
    numero_prateleira = models.IntegerField()


class Lote(models.Model):
    id_usuario = models.ForeignKey(Usuario,
                                   default='00',
                                   on_delete=models.SET_DEFAULT,
                                   verbose_name='Usuario criador')
    id_produto = models.ForeignKey(Produto,
                                   on_delete=models.CASCADE,
                                   verbose_name='ID Produto')
    quantidade = models.IntegerField()
    observacoes = models.CharField(max_length=100)
    data_fabricacao = models.DateField()
    data_vencimento = models.DateField(blank=True, null=True)
