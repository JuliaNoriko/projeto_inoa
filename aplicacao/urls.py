from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ativos/', views.adicionar_ativo, name='ativos'),
    path('informacoes_ativos/', views.informacoes_ativos, name='informacoes_ativos'),
    path('cotacoes/', views.listar_cotacoes, name='cotacoes'),
]
