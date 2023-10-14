import smtplib
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime
import email.message

db_url = "mysql://mbaGrupo1:mba-es-25-grupo-01@jdbc:mysql://coincap-data-engineering.cuh8tdvoemfc.us-east-1.rds.amazonaws.com:3306/coincap"

msg = email.message.Message()
smtp_password = "ucmfizgmnsalqflq"
sender_email = "projectdataengineering@gmail.com"
receiver_email = "projectdataengineering@gmail.com"

target_price = 130000

def get_bitcoin_price_from_database():
    try:
        connection = mysql.connector.connect(
            host=db_url
        )
        cursor = connection.cursor()
        query = "SELECT priceBRL, timestamp FROM bitcoin ORDER BY timestamp DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            priceBRL, timestamp = result
            return float(priceBRL), timestamp
        else:
            return None
    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {str(e)}")
        return None
    finally:
        cursor.close()
        connection.close()

def send_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

s = smtplib.SMTP ('smtp.gmail.com: 587')
s.starttls ()
s.login(msg['From'],smtp_password)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')


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
