import requests
import logging
from .models import Cotacao

logger = logging.getLogger(__name__)
logger.debug("Teste de log - Iniciando a função consultar_preco_ativo")


#Utilizando a API gratuita e pública da Twelve Data 
def Buscar_Cotacao_Ativo(simbolo):
    #Alpha vantage
    #API_KEY = '49499QIYXUDH83SD' 
    #url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={simbolo}&interval=1min&apikey={API_KEY}' #preencher com a url da API
    
    #Twelve data
    API_KEY = '9857a9ca763941a49994968188730fa2'
    url = f'https://api.twelvedata.com/time_series?apikey={API_KEY}&interval=1min&symbol={simbolo}'

    logger.debug(f"Enviando requisição para a API: {url}")
    response = requests.get(url)
    data = response.json()
    
    print(data)

    if 'values' in data:
        # Pegar o primeiro item da lista de valores
        ultima_cotacao = data['values'][0]
        # Extrair os valores desejados
        
       
        symbol = data['meta']['symbol']
        close_price = ultima_cotacao['close']
        low_price = ultima_cotacao['low']
        high_price = ultima_cotacao['high']
        datetime = ultima_cotacao['datetime']

        logger.debug(f"Simbol: {symbol}")
        logger.debug(f"close: {close_price}")
        logger.debug(f"high: {high_price}")
        logger.debug(f"low: {low_price}")
        logger.debug(f"datetime: {datetime}")
        
        resultado = {
                        'symbol': symbol,
                        'close': close_price,
                        'low': low_price,
                        'high': high_price,
                        'datetime': datetime
                    }

        return resultado
        
    else:
       return none

    # if response.status_code == 200:
    #     data = response.json()
    #     if 'values' in data:
    #         for item in data:
    #             cotacao, created = Cotacao.ativo.objects.get_or_create(nome=item['symbol'])
    #             Cotacao.preco = item['price']
    #             Cotacao.save()
    #             logger.debug(f"Preço do ativo {item['symbol']} atualizado para {item['price']}")

    # else:
    #     print(f"Erro: {response.status_code}")
    #     logger.error(f"Erro ao consultar a API: {response.status_code}")


def iniciar_tarefas():

    from django_q.models import Schedule 
    from django_q.tasks import schedule

    if not Schedule.objects.filter(func='aplicacao.tasks.Verificar_Cotacoes').exists():
        schedule(
            'aplicacao.tasks.Verificar_Cotacoes',
            schedule_type='I',
            minutes=5
        )