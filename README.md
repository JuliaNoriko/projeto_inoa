Case INOA

# Monitoramento de ativos
Esse projeto é um sistema feito com Python e Django, para monitorar as cotações de ativos da bolsa.
Nele foram feitas 4 páginas web: 
  - Página Inicial
  - Adicionar o ativo que será monitorado
  - Listar Informações dos ativos que estão sendo monitorados
  - Listar as cotações monitoradas de um ativo específico

Para adicionar o ativo que deseja monitorar basta preencher o formulário em 'Adicionar Ativo' preechendo todos os requisitos que serão utilizados durante o monitoramento, como simbolo, descrição, limite inferior, limite superior, periodicidade em minutos.

Depois de preencher é possível acompanhar quais ativos foram adicionados no monitoramento em 'Listar Informações Ativos' ou então visualizar as cotações que foram registradas de um ativo em específico em 'Listar Cotações'.

O monitoramento da lista de ativos é feita e armazenada no banco de dados a cada 5 minutos(para não sobrecarregar a API de consulta de ativo, uma vez que podemos fazer apenas 8 requisições por minuto na versão gratuita do twelve data), nesse primeiro momento.

Foi utilizado o túnel de preço estático, no qual o investidor insere juntamente com as demais informações do Ativo, qual o limite superior e inferior que será utilizado.

Assim, caso a cotação de um ativo seja maior que o limite superior estipulado no cadastro do ativo, será enviado um e-mail alertando o investidor que o ativo monitorado está com oportunidade de venda ou então caso a cotação seja menor que o limite inferior estipulado, será enviado um e-mail alertando o investidor que o ativo está com oportunidade de compra.

OBS: O envio de e-mail ainda não está totalmente funcional, uma vez que a conexão está sendo negada pelo provedor do gmail, por isso essa parte está comentada no código.


### Pré-requisitos

- Python 3.8+
- Django 3.2
- Django q 1.3.9

### Passos

1. Clone o repositório:
    ```sh
    git clone https://github.com/JuliaNoriko/projeto_inoa.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd desafio_inoa
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o seguinte comando para iniciar o servidor Django:
```sh
python manage.py runserver
```

2. Execute em outro prompt para rodar o worker que processará a fila de tarefas, que permite o monitoramento dos ativos
```sh
python manage.py qcluster
```

3. No seu navegador acesse o servidor:
```sh
http://127.0.0.1:8000/
