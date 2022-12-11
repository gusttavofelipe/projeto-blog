from django import template

register = template.Library()


# registrando filtro
@register.filter(name='comentfilter')
def plural(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)

        if num_comentarios == 1:
            return f'{num_comentarios} comentário'

        elif num_comentarios > 1:
            return f'{num_comentarios} comentários'
        
        else:
            return f'Nenhum comentário'
    except:
        return f'{num_comentarios} comentário(s)'