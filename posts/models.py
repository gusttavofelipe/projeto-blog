from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now(), verbose_name='Data postada')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=True, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.redimensionar_img(self.imagem_post.name, 800)


    @staticmethod
    def redimensionar_img(nome_img, nova_largura): # executa ao salvar a imagem
        caminho_img = os.path.join(settings.MEDIA_ROOT, nome_img)
        img = Image.open(caminho_img) 
        largura, altura = img.size
        nova_altura = round((nova_largura * altura) / largura)

        if largura <= nova_largura:
            img.close()
            return

        nova_img = img.resize((nova_largura, nova_altura), Image.ANTIALIAS)        
        nova_img.save(caminho_img, optimize=True, quality=60)