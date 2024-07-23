#Comando para consultar o banco de dados do django:
#python manage.py shell


# from aplicacao.utils import Buscar_Cotacao_Ativo
# from aplicacao.tasks import Verificar_Cotacoes
# Verificar_Cotacoes()

#$ python manage.py shell

#Digitar os comandos abaixo para as consultas do bd
from aplicacao.models import Ativo, Cotacao

todos_ativos = Ativo.objects.all()
for ativos in todos_ativos:
    print(ativos)


todos_parametros = ParametroAtivo.objects.all()
for parametros in todos_parametros:
    print(parametros)

    
todas_cotacao = Cotacao.objects.all()
for cotacao in todas_cotacao:
    print(cotacao)