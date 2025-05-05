
import ccxt
import os
import time
from datetime import datetime

def get_close_price():
    api_key = os.getenv('HTX_API_KEY')
    api_secret = os.getenv('HTX_API_SECRET')

    exchange = ccxt.huobi({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True
    })

    symbol = 'ETH/USDT'
    timeframe = '1m'

    # Получаем последнюю 1 свечу
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=1)[0]

    timestamp = datetime.utcfromtimestamp(ohlcv[0] / 1000).isoformat() + 'Z'
    close_price = ohlcv[4]

    return timestamp, close_price

def write_to_file(timestamp, close_price):
    line = f"{timestamp}, ETH/USDT, close: {close_price}\n"
    with open("data_log.txt", "a") as file:
        file.write(line)
    print("Записано:", line.strip())

if __name__ == "__main__":
    print("DATA ENGINE 0.4 запущен. Сбор данных каждую минуту.")
    while True:
        try:
            timestamp, close_price = get_close_price()
            write_to_file(timestamp, close_price)
        except Exception as e:
            print("Ошибка:", e)
        time.sleep(60)
