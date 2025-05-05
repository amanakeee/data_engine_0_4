
import ccxt
import time
import os
import pandas as pd
from datetime import datetime

# Load environment variables for API keys
API_KEY = os.getenv('HTX_API_KEY')
API_SECRET = os.getenv('HTX_API_SECRET')

# Initialize the exchange
exchange = ccxt.huobi({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

# Define the trading symbol and the file to store the data
symbol = 'BTC/USDT'
filename = 'data_log.txt'

def fetch_data():
    try:
        # Fetch ticker data from the exchange
        ticker = exchange.fetch_ticker(symbol)
        return ticker
    except ccxt.BaseError as e:
        print(f"Error fetching data from exchange: {e}")
        return None

def write_data_to_file(data):
    # Convert the data into a readable format
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data = f"{timestamp}, {data['symbol']}, {data['last']}, {data['high']}, {data['low']}, {data['bid']}, {data['ask']}
"
    
    # Write to the log file
    with open(filename, 'a') as file:
        file.write(log_data)

def main():
    while True:
        data = fetch_data()
        if data:
            write_data_to_file(data)
        time.sleep(60)  # Fetch new data every 60 seconds

if __name__ == "__main__":
    main()
