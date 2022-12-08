from django.db.models import Q, Case, When, Count
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from categorias.models import Categoria
from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

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
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario # formulario de detalhes do post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()  
        comentarios = Comentario.objects.filter(
            publicado_comentario=True, post_comentario=post.id)

        contexto['comentarios'] = comentarios     

        return contexto

    def form_valid(self, form):
        post = self.get_object()    
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated: 
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário enviado.')

        return redirect('post_detalhes', pk=post.id)