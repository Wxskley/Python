import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor de email
host = "smtp.example.com"
port = 587
usuario = "seu_email@example.com"
senha = "sua_senha"


# Função para enviar um email
def enviar_email(destinatario, assunto, mensagem):
    # Configura o email
    email = MIMEMultipart()
    email["From"] = usuario
    email["To"] = destinatario
    email["Subject"] = assunto

    # Adiciona o corpo da mensagem
    corpo = MIMEText(mensagem, "plain")
    email.attach(corpo)

    # Conecta-se ao servidor de email
    servidor = smtplib.SMTP(host, port)
    servidor.starttls()
    servidor.login(usuario, senha)

    # Envia o email
    servidor.send_message(email)
    servidor.quit()


# Exemplo de uso
destinatario = "destinatario@example.com"
assunto = "Teste de Email"
mensagem = "Olá, este é um teste de email enviado usando Python."

enviar_email(destinatario, assunto, mensagem)
