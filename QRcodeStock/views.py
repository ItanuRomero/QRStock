from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    context = {'titulo': 'QRStock - Home'}
    return render(request, 'base.html', context)


def login(request):
    context = {'titulo': 'QRStock - Login'}
    return render(request, '', context)


@login_required
def list_products(request):
    return render(request, '')


@login_required
def show_product(request):
    return render(request, '')


@login_required
def edit_product(request):
    return render(request, '')


@login_required
def add_product(request):
    return render(request, '')


@login_required
def list_categories(request):
    return render(request, '')


@login_required
def show_category(request):
    return render(request, '')


@login_required
def edit_category(request):
    return render(request, '')


@login_required
def add_category(request):
    return render(request, '')


@login_required
def list_shelves(request):
    return render(request, '')


@login_required
def show_shelf(request):
    return render(request, '')


@login_required
def edit_shelf(request):
    return render(request, '')


@login_required
def add_shelf(request):
    return render(request, '')


@login_required
def list_lots(request):
    return render(request, '')


@login_required
def show_lot(request):
    return render(request, '')


@login_required
def edit_lot(request):
    return render(request, '')


@login_required
def add_lot(request):
    return render(request, '')


@login_required
def list_users(request):
    return render(request, '')


def show_user(request):
    return render(request, '')


def edit_user(request):
    return render(request, '')


def add_user(request):
    return render(request, '')
