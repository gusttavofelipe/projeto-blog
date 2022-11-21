from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat') 
    list_display_links = ('id', 'nome_cat') # links clicaveis

admin.site.register(Categoria, CategoriaAdmin) # registrando 