from forex_python.converter import CurrencyRates
from datetime import datetime
from decimal import Decimal


def convert_USD_to_BRL(price_usd):
    currency = CurrencyRates()
    return int(currency.convert("USD", "BRL", Decimal(price_usd)))


def convert_UNIX_timestamp(unix_timestamp):
    return datetime.fromtimestamp(int(unix_timestamp/1000))
