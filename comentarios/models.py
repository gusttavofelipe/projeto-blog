from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Autor')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Selecionar Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário usuário')
    data_comentario = models.DateField(default=timezone.now(), verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False)

def __str__(self):
    return self.nome_comentario
