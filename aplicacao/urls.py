from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ativos/', views.adicionar_ativo, name='ativos'),
    path('parametros_preco/', views.adicionar_parametro, name='parametros_preco'),
    path('cotacoes/', views.listar_cotacoes, name='cotacoes'),
]
