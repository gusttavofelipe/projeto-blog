from django.forms import ModelForm
from .models import Comentario
import requests

class FormComentario(ModelForm): # formulario de detalhes do post

    def clean(self): # fazer validações
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        if not recaptcha_response:
            self.add_error(
                'comentario',
                'Confirme que você não é um robô.'
            )
        
        # https://google.com/recaptcha/api/siteverify
        # secret
        # response

        recaptcha_request = requests.post(
            'https://google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdOt5AjAAAAAEURQl4apQdT0tEUTYsaYKrjTvei',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()
        # print(recaptcha_result)

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario') 
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario', 'usuario_comentario',)