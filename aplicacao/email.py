from django.core.mail import send_mail
from django.conf import settings

def enviar_email(tipo):
    if tipo=='compra':
        assunto = 'Monitoramento de Ativos'
        mensagem = 'Olá, estou enviando esse e-mail para avisar que o ativo que estamos monitorando está com oportunidade de Compra!'
        
    else:
        assunto = 'Monitoramento de Ativos'
        mensagem = 'Olá, estou enviando esse e-mail para avisar que o ativo que estamos monitorando está com oportunidade de Venda!'

    from_email = settings.DEFAULT_FROM_EMAIL
    destinatario = ['exemplo@gmail.com']
    send_mail(assunto, mensagem, from_email, destinatario)