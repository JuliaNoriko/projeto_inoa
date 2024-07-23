import requests
import logging
from .models import Cotacao

logger = logging.getLogger(__name__)
logger.debug("Teste de log - Iniciando a função Buscar_Cotacao_Ativo")


#Utilizando a API gratuita e pública da Twelve Data 
def Buscar_Cotacao_Ativo(simbolo, intervalo):
    #Alpha vantage
    #API_KEY = '49499QIYXUDH83SD' 
    #url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={simbolo}&interval=1min&apikey={API_KEY}' #preencher com a url da API
    
    #Twelve data
    API_KEY = '9857a9ca763941a49994968188730fa2'
    url = f'https://api.twelvedata.com/time_series?apikey={API_KEY}&interval={intervalo}min&symbol={simbolo}'

    logger.debug(f"Enviando requisição para a API: {url}")
    response = requests.get(url)
    data = response.json()
    
    #print(data)

    if 'values' in data:
        # Pegar o primeiro item da lista de valores
        ultima_cotacao = data['values'][0]
        # Extrair os valores desejados
        
       
        symbol = data['meta']['symbol']
        close_price = ultima_cotacao['close']
        datetime = ultima_cotacao['datetime']

        logger.debug(f"Simbol: {symbol}")
        logger.debug(f"close: {close_price}")
        logger.debug(f"datetime: {datetime}")
        
        resultado = {
                        'symbol': symbol,
                        'close': close_price,
                        'datetime': datetime
                    }

        return resultado
        
    else:
       return None

#Funcao para chamar a requisição API
def iniciar_tarefas():

    from django_q.models import Schedule 
    from django_q.tasks import schedule

    if not Schedule.objects.filter(func='aplicacao.tasks.Verificar_Cotacoes').exists():
        schedule(
            'aplicacao.tasks.Verificar_Cotacoes',
            schedule_type='I',
            minutes=5
        )