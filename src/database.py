import mysql.connector
from mysql.connector import errorcode
import os


config = {
    "host": os.environ['DATABASE_HOST'],
    "user": os.environ['DATABASE_USER'],
    "password": os.environ['DATABASE_PASSWORD'],
    "database": os.environ['DATABASE_NAME']
}


def connect_to_database():
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acesso negado: senha ou usuário incorretos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("O banco de dados que você está querendo se conectar não existe")
        else:
            print(f"Erro ao conectar no banco de dados: {str(err)}")
    return None


def insert_bitcoin_data(data):
    connection = connect_to_database()
    cursor = connection.cursor()
    update_table = (
        "INSERT INTO bitcoin (id, timestamp, `rank`, symbol, name, priceBRL)"
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(update_table, (
        data["id"],
        data["timestamp"],
        data["rank"],
        data["symbol"],
        data["name"],
        data["priceBRL"]
    ))
    connection.commit()
    cursor.close()
    connection.close()


def get_bitcoin_price_from_database():
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT priceBRL, timestamp FROM bitcoin ORDER BY timestamp DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        priceBRL, timestamp = result
        return float(priceBRL), timestamp
    else:
        return None
