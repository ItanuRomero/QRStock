from django.forms import ModelForm
from .models import Usuario, Produto, Estante, Categoria, Lote


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'



class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class FormEstante(ModelForm):
    class Meta:
        model = Estante
        fields = '__all__'


class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class FormLote(ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'