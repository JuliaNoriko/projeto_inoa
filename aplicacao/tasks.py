from .models import ParametroAtivo, Cotacao
from .utils import Buscar_Cotacao_Ativo
from decimal import Decimal

def Verificar_Cotacoes():

    from django_q.tasks import schedule, Schedule

    parametros = ParametroAtivo.objects.all()

    for parametro in parametros:
        preco = Buscar_Cotacao_Ativo(parametro.ativo, parametro.periodicidade)

        print(preco)

        if preco:
            cotacao = Cotacao(
                ativo = parametro.ativo,
                preco = preco['close'],
                data_hora = preco['datetime']
            )     
            cotacao.save()   
            print(f'Cotação salva: {cotacao}') 

        #Verificando se o último preço do Ativo é maior que o limite superior ou menor que o limite inferior para avisar o investidor
            if Decimal(preco['close']) < parametro.limite_inferior:
                print(f'Comprar ação!')

            elif Decimal(preco['close']) > parametro.limite_superior:
                print(f'Vender ação!')