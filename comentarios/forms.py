from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm): # formulario de detalhes do post

    def clean(self): # fazer validações
        data = self.cleaned_data
        nome = data.get('nome_comentario') 
        email = data.get('email_comentario')
        comentario = data.get('comentario')


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario', 'usuario_comentario',)