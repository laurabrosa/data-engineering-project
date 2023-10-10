import requests

def collect_bitcoin_data(): 
    data = requests.get("api.coincap.io/v2/assets/bitcoin")
return data