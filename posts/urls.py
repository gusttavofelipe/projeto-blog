from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'), # home
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'), # categorias > categoria
    path('busca/', views.PostBusca.as_view(), name='post_busca'), # busca termo
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'), # post > primary key (id)
]
