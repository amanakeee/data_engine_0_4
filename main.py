
import requests
import time
import json
import logging

# Configuring logging
logging.basicConfig(filename="bot_log.csv", level=logging.INFO)
logger = logging.getLogger()

# URL for market data
url = "https://api.huobi.pro/market/detail?symbol=btcusdt"

# The loop to get data and write to the log
while True:
    try:
        response = requests.get(url)
        data = response.json()["data"]
        
        # Getting current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        # Preparing the log data
        log_data = f"{timestamp}, {data['symbol']}, {data['last']}, {data['high']}, {data['low']}, {data['bid']}, {data['ask']}"

        # Logging the data
        logger.info(log_data)

        # Sleep for 5 seconds before the next request
        time.sleep(5)
        
    except Exception as e:
        logger.error(f"Error: {e}")
        time.sleep(5)  # Wait before retrying in case of error
