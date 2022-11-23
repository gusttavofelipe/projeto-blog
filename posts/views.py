from .models import Post
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

class PostIndex(ListView):
    model = Post # indicando model
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'


class PostBusca(ListView):
    pass


class PostCategoria(ListView):
    pass


class PostDetalhes(UpdateView):
    pass