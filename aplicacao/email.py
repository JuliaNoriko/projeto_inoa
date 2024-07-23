import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def enviar_email(destinatario, assunto, corpo):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    # email_usuario = os.getenv('EMAIL_USUARIO')
    # email_senha = os.getenv('EMAIL_SENHA')
    email_usuario = 'noriko.julia@gmail.com'
    email_senha = 'SenhaDificilPara1402'

    msg = MIMEMultipart()
    msg['From'] = email_usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    #Corpo do email
    msg.attach(MIMEText(corpo, 'plain'))

    #Tentando enviar o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_usuario, email_senha)
        texto = msg.as_string()
        server.sendmail(email_usuario, destinatario, texto)
        server.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Falha ao enviar e-mail: {e}')

    