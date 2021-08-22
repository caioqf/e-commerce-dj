from django.contrib import admin
from .models import Produto, Categoria


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'marca', 'modelo', 'categoria', 'preco')
    list_display_links = ('id', 'nome', 'marca', 'modelo', 'preco')
    search_fields = ('id', 'nome', 'marca', 'modelo')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
