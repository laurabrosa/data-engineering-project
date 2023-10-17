import smtplib
from datetime import datetime
import email.message
import database
import os
import time
import schedule

smtp_password = os.environ['SMTP_PASSWORD']
sender_email = os.environ['SENDER_EMAIL']
receiver_email = os.environ['RECEIVER_EMAIL']

target_price = 130000


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
        s.sendmail(sender_email, [receiver_email],
                   msg.as_string().encode('utf-8'))
        print('Email enviado')
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar o email: {str(e)}")
    finally:
        s.quit()


def data_analysis():
    result = database.get_bitcoin_price_from_database()
    if result:
        priceBRL, timestamp = result
        if priceBRL < target_price:
            subject = "Alerta de Preço do Bitcoin"
            message = f"Preço de R${priceBRL:.2f} em {timestamp}"
            send_email(subject, message)
        print(f"Preço do Bitcoin em {timestamp}: R${priceBRL:.2f}")


schedule.every().minutes.do(data_analysis)

while True:
    schedule.run_pending()
    time.sleep(1)
