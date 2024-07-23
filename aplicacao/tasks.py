from .models import Cotacao, Ativo
from .utils import Buscar_Cotacao_Ativo
from decimal import Decimal
from .email import enviar_email
# from .credentials import Definir_Credenciais

destinatario = 'noriko.julia@gmail.com'
assunto = 'Monitoramento de Ativos'
corpo_venda = 'Olá, estou enviando esse e-mail para avisar que o ativo que estamos monitorando está com oportunidade de Venda!'
corpo_compra = 'Olá, estou enviando esse e-mail para avisar que o ativo que estamos monitorando está com oportunidade de Compra!'

def Verificar_Cotacoes():

    from django_q.tasks import schedule, Schedule

    parametros = Ativo.objects.all()

    for parametro in parametros:
        preco = Buscar_Cotacao_Ativo(parametro.simbolo, parametro.periodicidade)

        if preco:
            cotacao = Cotacao(
                ativo = parametro,
                preco = preco['close'],
                data_hora = preco['datetime']
            )     
            cotacao.save()   
            #print(f'Cotação salva: {cotacao}') 

        #Verificando se o último preço do Ativo é maior que o limite superior ou menor que o limite inferior para avisar o investidor
            if Decimal(preco['close']) < parametro.limite_inferior:
                enviar_email(destinatario, assunto, corpo_compra)
                print(f'Comprar ação!')

            elif Decimal(preco['close']) > parametro.limite_superior:
                enviar_email(destinatario, assunto, corpo_venda)
                print(f'Vender ação!')
            
            else:
                print(f'Está entre os limites')
                enviar_email(destinatario, assunto, corpo_venda)