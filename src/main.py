import time
import schedule
import requests
import database
import helpers


def fetch_bitcoin_data():
    response = requests.get("http://api.coincap.io/v2/assets/bitcoin")
    data = response.json()
    price_value = helpers.convert_USD_to_BRL(data["data"]["priceUsd"])

    if response.status_code == 200:
        bitcoin_data = {
            "id": data["data"]["id"],
            "timestamp": helpers.convert_UNIX_timestamp(data["timestamp"]),
            "rank": int(data["data"]["rank"]),
            "symbol": data["data"]["symbol"],
            "name": data["data"]["name"],
            "priceBRL": price_value
        }

        database.insert_bitcoin_data(bitcoin_data)
        print("Data inserted with success!")


schedule.every().minutes.do(fetch_bitcoin_data)

while True:
    schedule.run_pending()
    time.sleep(1)
