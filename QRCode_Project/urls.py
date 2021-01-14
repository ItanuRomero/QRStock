"""QRCode_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from QRcodeStock.views import home, login, \
    list_products, show_product, add_product, edit_product, delete_product, \
    list_categories, show_category, add_category, edit_category, delete_category, \
    list_shelves, show_shelf, add_shelf, edit_shelf, delete_shelf, \
    list_lots, show_lot, add_lot, edit_lot, delete_lot,\
    list_users, show_user, add_user, edit_user, delete_user,\
    Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('login/', login, name='url_login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='url_register'),
]

# urls de produto
urlpatterns += [
    path('products/', list_products, name='url_list_products'),
    path('product/<int:id>', show_product, name='url_show_product'),
    path('add_product/', add_product, name='url_add_product'),
    path('edit_product/<int:id>', edit_product, name='url_edit_product'),
    path('delete_product/<int:id>', delete_product, name='url_delete_product'),
]

# urls de categoria
urlpatterns += [
    path('categories/', list_categories, name='url_list_categories'),
    path('category/<int:id>', show_category, name='url_show_category'),
    path('add_category/', add_category, name='url_add_category'),
    path('edit_category/<int:id>', edit_category, name='url_edit_category'),
    path('delete_category/<int:id>', delete_category, name='url_delete_category'),
]

# urls de estante
urlpatterns += [
    path('shelves/', list_shelves, name='url_list_shelves'),
    path('shelf/<int:id>', show_shelf, name='url_show_shelf'),
    path('add_shelf/', add_shelf, name='url_add_shelf'),
    path('edit_shelf/<int:id>', edit_shelf, name='url_edit_shelf'),
    path('delete_shelf/<int:id>', delete_shelf, name='url_delete_shelf'),
]

# urls de lote
urlpatterns += [
    path('lots/', list_lots, name='url_list_lots'),
    path('lot/<int:id>', show_lot, name='url_show_lot'),
    path('add_lot/', add_lot, name='url_add_lot'),
    path('edit_lot/<int:id>', edit_lot, name='url_edit_lot'),
    path('delete_lot/<int:id>', delete_lot, name='url_delete_lot'),
]

# urls de usuario
urlpatterns += [
    path('users/', list_users, name='url_list_users'),
    path('user/<int:id>', show_user, name='url_show_user'),
    path('add_user/', add_user, name='url_add_user'),
    path('edit_user/<int:id>', edit_user, name='url_edit_user'),
    path('delete_user/<int:id>', delete_user, name='url_delete_user'),
]
