import mysql.connector
from mysql.connector import errorcode
import os

config = {
    "host": os.environ['DATABASE_HOST'],
    "user": os.environ['DATABASE_USER'],
    "password": os.environ['DATABASE_PASSWORD'],
    "database": os.environ['DATABASE_NAME']
}


def insert_bitcoin_data(data):
    try:
        connection = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        update_table = (
            "INSERT INTO bitcoin (id, timestamp, `rank`, symbol, name, priceBRL)"
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        cursor = connection.cursor()
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
