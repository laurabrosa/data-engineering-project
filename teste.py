import mysql.connector

# Configurações da conexão
db_config = {
    "host": "coincap-data-engineering.cuh8tdvoemfc.us-east-1.rds.amazonaws.com",
    "user": "mbaGrupo1",
    "password": "mba-es-25-grupo-01",
    "database": "coincap",
}

try:
    # Estabelecer a conexão com o banco de dados
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Conexão bem-sucedida!")

    # Fechar a conexão
    connection.close()

except mysql.connector.Error as error:
    print(f"Erro ao conectar ao banco de dados: {error}")
