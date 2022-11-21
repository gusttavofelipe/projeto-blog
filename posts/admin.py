from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_post', 'autor_post', 'data_post',
                    'categoria_post', 'publicado_post', )

    list_editable = ('publicado_post', ) # torna o campo editavel 
    list_display_links = ('id', 'titulo_post',) # torna o campo clicavel
    summernote_fields = ('conteudo_post', )

admin.site.register(Post, PostAdmin)