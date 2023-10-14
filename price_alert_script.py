import smtplib
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime
import email.message

# Configurações da conexão com o banco de dados
db_config = {
    "host": "coincap-data-engineering.cuh8tdvoemfc.us-east-1.rds.amazonaws.com",
    "user": "mbaGrupo1",
    "password": "mba-es-25-grupo-01",
    "database": "coincap",
}

smtp_password = "ucmfizgmnsalqflq"
sender_email = "projectdataengineering@gmail.com"
receiver_email = "projectdataengineering@gmail.com"

target_price = 130000

def get_bitcoin_price_from_database():
    try:
        # Estabelecer a conexão com o banco de dados
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT priceBRL, timestamp FROM bitcoin ORDER BY timestamp DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            priceBRL, timestamp = result
            return float(priceBRL), timestamp
        else:
            return None
    except mysql.connector.Error as e:
        print(f"Erro ao consultar o banco de dados: {str(e)}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def send_email(subject, message):
    msg = email.message.Message()
    msg.set_payload(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    try:
        s.login(sender_email, smtp_password)
        s.sendmail(sender_email, [receiver_email], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar o email: {str(e)}")
    finally:
        s.quit()

if __name__ == "__main__":
    result = get_bitcoin_price_from_database()

    if result:
        priceBRL, timestamp = result
        current_datetime = datetime.now()

        if priceBRL < target_price:
            subject = "Alerta de Preço do Bitcoin"
            message = f"Preço de R${priceBRL:.2f} em {timestamp}"
            send_email(subject, message)

        print(f"Preço do Bitcoin em {timestamp}: R${priceBRL:.2f}")
