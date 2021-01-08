from django.contrib import admin
from .models import Estante, Categoria, Lote, Usuario, Produto
# Register your models here.

admin.site.register(Estante)
admin.site.register(Categoria)
admin.site.register(Lote)
admin.site.register(Usuario)
admin.site.register(Produto)
