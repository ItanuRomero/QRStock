from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from QRcodeStock.forms import FormProduto, \
    FormCategoria, FormLote, FormEstante, \
    FormUsuario
from QRcodeStock.models import Produto, Categoria, \
    Estante, Lote, Usuario


def home(request):
    context = {'titulo': 'QRStock - Home'}
    return render(request, 'home.html', context)


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def login(request):

    return render(request, 'registration/login.html')


@login_required
def list_products(request):
    categories = Categoria.objects.all()
    if request.POST:
        if request.POST['filter']:
            products = Produto.objects.filter(nome=request.POST['filter'])
        else:
            products = Produto.objects.all()
        if request.POST['category-filter']:
            if request.POST['category-filter'] != 0:
                products = Produto.objects.filter(id_categoria=request.POST['category-filter'])
        else:
            products = Produto.objects.all()
    else:
        products = Produto.objects.all()
    context = {'titulo': 'QRStock - Lista de produtos', 'products': products, 'categories': categories}
    return render(request, 'listagem/produtos.html', context)


@login_required
def show_product(request, id):
    product = Produto.objects.get(id=id)
    context = {'titulo': 'QRStock - Produto', 'produto': product}
    return render(request, 'show/produto.html', context)


@login_required
def edit_product(request, id):
    selected_product = Produto.objects.get(id=id)
    form = FormProduto(request.POST or None, request.FILES or None, instance=selected_product)
    contexto = {'titulo': 'QRStock - Editar produto',
                'form': form, 'acao': 'Editar produto',
                'redirect_url': '/products/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Produto atualizado com sucesso!")
        return redirect('url_list_products')
    else:
        return render(request, 'edit/edit_and_create.html', contexto)


@login_required
def add_product(request):
    form = FormProduto(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar produto',
               'form': form, 'acao': 'Criar produto',
               'redirect_url': '/products/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Produto criado com sucesso!")
        return redirect('url_list_products')
    else:
        return render(request, 'edit/edit_and_create.html', context)


@login_required
def delete_product(request, id):
    product = Produto.objects.get(id=id)
    context = {'registro': product.nome, 'redirect': '/products/'}
    if request.method == 'POST':
        product.delete()
        return redirect('url_list_products')
    else:
        return render(request, 'delete/confirm.html', context)


@login_required
def list_categories(request):
    if request.POST:
        if request.POST['filter']:
            categories = Categoria.objects.filter(nome=request.POST['filter'])
        else:
            categories = Categoria.objects.all()
    else:
        categories = Categoria.objects.all()
    context = {'titulo': 'QRStock - Lista de categorias', 'categories': categories}
    return render(request, 'listagem/categorias.html', context)


@login_required
def show_category(request, id):
    category = Categoria.objects.get(id=id)
    context = {'titulo': 'QRStock - Categoria', 'categoria': category}
    return render(request, 'show/categoria.html', context)


@login_required
def edit_category(request, id):
    selected_category = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST or None, request.FILES or None, instance=selected_category)
    contexto = {'titulo': 'QRStock - Editar categoria', 'form': form,
                'acao': 'Editar categoria',
                'redirect_url': '/categories/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Categoria atualizada com sucesso!")
        return redirect('url_list_categories')
    else:
        return render(request, 'edit/edit_and_create.html', contexto)


@login_required
def add_category(request):
    form = FormCategoria(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar categoria', 'form': form,
               'acao': 'Editar categoria',
               'redirect_url': '/categories/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Categoria criada com sucesso!")
        return redirect('url_list_categories')
    else:
        return render(request, 'edit/edit_and_create.html', context)


@login_required
def delete_category(request, id):
    category = Categoria.objects.get(id=id)
    context = {'registro': category.nome, 'redirect': '/categories/'}
    if request.method == 'POST':
        category.delete()
        return redirect('url_list_categories')
    else:
        return render(request, 'delete/confirm.html', context)


@login_required
def list_shelves(request):
    if request.POST:
        if request.POST['filter']:
            shelves = Estante.objects.filter(codigo=request.POST['filter'])
        else:
            shelves = Estante.objects.all()
    else:
        shelves = Estante.objects.all()
    context = {'titulo': 'QRStock - Lista de estantes', 'shelves': shelves}
    return render(request, 'listagem/estantes.html', context)


@login_required
def show_shelf(request, id):
    shelf = Estante.objects.get(id=id)
    context = {'titulo': 'QRStock - Estante', 'shelf': shelf}
    return render(request, 'show/estante.html', context)


@login_required
def edit_shelf(request, id):
    selected_shelf = Estante.objects.get(id=id)
    form = FormEstante(request.POST or None, request.FILES or None, instance=selected_shelf)
    contexto = {'titulo': 'QRStock - Editar estante', 'form': form,
                'acao': 'Editar estante',
                'redirect_url': '/shelves/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Estante atualizada com sucesso!")
        return redirect('url_list_shelves')
    else:
        return render(request, 'edit/edit_and_create.html', contexto)


@login_required
def add_shelf(request):
    form = FormEstante(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar estante', 'form': form,
               'acao': 'Criar estante',
               'redirect_url': '/shelves/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Estante criada com sucesso!")
        return redirect('url_list_shelves')
    else:
        return render(request, 'edit/edit_and_create.html', context)


@login_required
def delete_shelf(request, id):
    shelf = Estante.objects.get(id=id)
    context = {'registro': shelf.codigo, 'redirect': '/shelves/'}
    if request.method == 'POST':
        shelf.delete()
        return redirect('url_list_shelves')
    else:
        return render(request, 'delete/confirm.html', context)


@login_required
def list_lots(request):
    if request.POST:
        if request.POST['filter']:
            lots = Lote.objects.filter(id=request.POST['filter'])
        else:
            lots = Lote.objects.all()
    else:
        lots = Lote.objects.all()
    context = {'titulo': 'QRStock - Lista de lotes', 'lots': lots}
    return render(request, 'listagem/lotes.html', context)


@login_required
def show_lot(request, id):
    lot = Lote.objects.get(id=id)
    context = {'titulo': 'QRStock - Lote', 'lote': lot}
    return render(request, 'show/lote.html', context)


@login_required
def edit_lot(request, id):
    selected_lot = Lote.objects.get(id=id)
    form = FormLote(request.POST or None, request.FILES or None, instance=selected_lot)
    contexto = {'titulo': 'QRStock - Editar lote', 'form': form,
                'acao': 'Editar lote',
                'redirect_url': '/lots/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Lote atualizado com sucesso!")
        return redirect('url_list_lots')
    else:
        return render(request, 'edit/edit_and_create.html', contexto)


@login_required
def add_lot(request):
    form = FormLote(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar lote', 'form': form,
               'acao': 'Criar lote',
               'redirect_url': '/lots/'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Lote criado com sucesso!")
        return redirect('url_list_lots')
    else:
        return render(request, 'edit/edit_and_create.html', context)


@login_required
def delete_lot(request, id):
    lot = Lote.objects.get(id=id)
    context = {'registro': lot.nome, 'redirect': '/lots/'}
    if request.method == 'POST':
        lot.delete()
        return redirect('url_list_lots')
    else:
        return render(request, 'delete/confirm.html', context)


@login_required
def list_users(request):
    if request.POST:
        if request.POST['filter']:
            users = Usuario.objects.filter(nome=request.POST['filter'])
        else:
            users = Usuario.objects.all()
    else:
        users = Usuario.objects.all()
    context = {'titulo': 'QRStock - Lista de usuários', 'users': users}
    return render(request, 'listagem/usuarios.html', context)


@login_required
def show_user(request, id):
    user = Usuario.objects.get(id=id)
    context = {'titulo': 'QRStock - Usuário', 'user': user}
    return render(request, 'show/usuario.html', context)


def edit_user(request, id):
    if request.user.is_staff:
        selected_user = Usuario.objects.get(id=id)
        form = FormUsuario(request.POST or None, request.FILES or None, instance=selected_user)
        contexto = {'titulo': 'QRStock - Editar usuário', 'form': form,
                    'acao': 'Editar usuário',
                    'redirect_url': '/users/'}
        if form.is_valid():
            form.save()
            # messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('url_list_users')
        else:
            return render(request, 'edit/edit_and_create.html', contexto)
    else:
        contexto = {'titulo': 'QRStock - Erro',
                    'error': 'Você não tem permissão para executar este procedimento, '
                             'procure o seu gerente.'}
        return render(request, 'error.html', contexto)


def add_user(request):
    form = FormUsuario(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar usuário', 'form': form,
               'acao': 'Criar usuário',
               'redirect_url': '/accounts/login'}
    if form.is_valid():
        form.save()
        # messages.success(request, "Usuário criado com sucesso!")
        return redirect('url_list_users')
    else:
        return render(request, 'edit/edit_and_create.html', context)


@login_required
def delete_user(request, id):
    user = Usuario.objects.get(id=id)
    context = {'registro': user.nome, 'redirect': '/users/'}
    if request.method == 'POST':
        user.delete()
        return redirect('url_list_users')
    else:
        return render(request, 'delete/confirm.html', context)
