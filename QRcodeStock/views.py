from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from QRcodeStock.forms import FormProduto, FormCategoria, FormLote, FormEstante, FormUsuario
from QRcodeStock.models import Produto, Categoria, Estante, Lote, Usuario


def home(request):
    context = {'titulo': 'QRStock - Home'}
    return render(request, 'home.html', context)


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def login(request):
    context = {'titulo': 'QRStock - Login'}
    return render(request, 'registration/login.html', context)


@login_required
def list_products(request):
    if request.POST:
        if request.POST['filter']:
            products = Produto.objects.filter(nome=request.POST['filter'])
        else:
            products = Produto.objects.all()
    else:
        products = Produto.objects.all()
    context = {'titulo': 'QRStock - Lista de produtos', 'products': products}
    return render(request, 'QRcodeStock/', context)


@login_required
def show_product(request, id):
    product = Produto.objects.get(id=id)
    context = {'titulo': 'QRStock - Produto', 'produto': product}
    return render(request, 'QRcodeStock/', context)


@login_required
def edit_product(request, id):
    selected_product = Produto.objects.get(id=id)
    form = FormProduto(request.POST or None, request.FILES or None, instance=selected_product)
    contexto = {'titulo': 'QRStock - Editar produto', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Produto atualizado com sucesso!")
        return redirect('url_list_products')
    else:
        return render(request, 'QRcodeStock/', contexto)


@login_required
def add_product(request):
    form = FormProduto(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar produto', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Produto criado com sucesso!")
        return redirect('url_list_products')
    else:
        return render(request, 'QRcodeStock/', context)


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
    return render(request, 'QRcodeStock/', context)


@login_required
def show_category(request, id):
    category = Categoria.objects.get(id=id)
    context = {'titulo': 'QRStock - Categoria', 'Categoria': category}
    return render(request, 'QRcodeStock/', context)


@login_required
def edit_category(request):
    selected_category = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST or None, request.FILES or None, instance=selected_category)
    contexto = {'titulo': 'QRStock - Editar categoria', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Categoria atualizada com sucesso!")
        return redirect('url_list_categories')
    else:
        return render(request, 'QRcodeStock/', contexto)


@login_required
def add_category(request):
    form = FormCategoria(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar categoria', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Categoria criada com sucesso!")
        return redirect('url_list_categories')
    else:
        return render(request, 'QRcodeStock/', context)


@login_required
def list_shelves(request):
    if request.POST:
        if request.POST['filter']:
            shelves = Estante.objects.filter(codigo=request.POST['filter'])
        else:
            shelves = Estante.objects.all()
    else:
        shelves = Estante.objects.all()
    context = {'titulo': 'QRStock - Lista de Estantes', 'shelves': shelves}
    return render(request, 'QRcodeStock/', context)


@login_required
def show_shelf(request, id):
    shelf = Estante.objects.get(id=id)
    context = {'titulo': 'QRStock - Estante', 'shelf': shelf}
    return render(request, 'QRcodeStock/', context)


@login_required
def edit_shelf(request, id):
    selected_shelf = Estante.objects.get(id=id)
    form = FormEstante(request.POST or None, request.FILES or None, instance=selected_shelf)
    contexto = {'titulo': 'QRStock - Editar estante', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Estante atualizada com sucesso!")
        return redirect('url_list_shelves')
    else:
        return render(request, 'QRcodeStock/', contexto)


@login_required
def add_shelf(request):
    form = FormEstante(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar estante', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Estante criada com sucesso!")
        return redirect('url_list_shelves')
    else:
        return render(request, 'QRcodeStock/', context)


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
    return render(request, 'QRcodeStock/', context)


@login_required
def show_lot(request, id):
    lot = Lote.objects.get(id=id)
    context = {'titulo': 'QRStock - Lote', 'lote': lot}
    return render(request, 'QRcodeStock/', context)


@login_required
def edit_lot(request, id):
    selected_lot = Lote.objects.get(id=id)
    form = FormLote(request.POST or None, request.FILES or None, instance=selected_lot)
    contexto = {'titulo': 'QRStock - Editar lote', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Lote atualizado com sucesso!")
        return redirect('url_list_lots')
    else:
        return render(request, 'QRcodeStock/', contexto)


@login_required
def add_lot(request):
    form = FormLote(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar lote', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Lote criado com sucesso!")
        return redirect('url_list_lots')
    else:
        return render(request, 'QRcodeStock/', context)


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
    return render(request, 'QRcodeStock/', context)


@login_required
def show_user(request):
    user = Usuario.objects.get(id=id)
    context = {'titulo': 'QRStock - Usuário', 'user': user}
    return render(request, 'QRcodeStock/', context)


def edit_user(request, id):
    if request.user.is_staff:
        selected_user = Usuario.objects.get(id=id)
        form = FormUsuario(request.POST or None, request.FILES or None, instance=selected_user)
        contexto = {'titulo': 'QRStock - Editar usuário', 'form': form}
        if form.is_valid():
            form.save()
            # messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('url_list_users')
        else:
            return render(request, 'QRcodeStock/', contexto)
    else:
        contexto = {'titulo': 'QRStock - Erro', 'error': 'Você não tem permissão para executar este procedimento, '
                                                        'procure o seu gerente.'}
        return render(request, 'QRcodeStock/', contexto)


def add_user(request):
    form = FormUsuario(request.POST or None, request.FILES or None)
    context = {'titulo': 'QRStock - Adicionar usuário', 'form': form}
    if form.is_valid():
        form.save()
        # messages.success(request, "Usuário criado com sucesso!")
        return redirect('url_list_users')
    else:
        return render(request, 'QRcodeStock/', context)
