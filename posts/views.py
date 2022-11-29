from django.db.models import Q, Case, When, Count
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from categorias.models import Categoria
from django.shortcuts import render
from .models import Post

class PostIndex(ListView):
    model = Post # indicando model
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

    def get_queryset(self):
        qs =  super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True) # ordena posts em -id
        qs = qs.annotate( # conta numero de comentarios
            num_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context



class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            # buscando por termo nos campos
            Q(titulo_post__icontains=termo) | 
            Q(autor_post__first_name__iexact=termo) | 
            Q(conteudo_post__icontains=termo) | 
            Q(excerto_post__icontains=termo) | 
            Q(categoria_post__nome_cat__iexact=termo) 
        )
        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)  

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs
    

class PostDetalhes(UpdateView):
    pass