import requests
import json
from datetime import datetime
import os
import time

API_KEY = os.environ.get("FINNHUB_API_KEY")
print(f"API_KEY used: {API_KEY}")

# Full list of symbols extracted from your CSV (without trailing 'x')
SYMBOLS = ['ABT', 'ABBV', 'ACN', 'GOOGL', 'AMZN', 'AMBR', 'AAPL', 'APP', 'AZN', 'BAC', 'BRK.B', 'AVGO', 'CVX', 'CRCL', 'CSCO', 'KO', 'COIN', 'CMCSA', 'CRWD', 'DHR', 'DFDV', 'LLY', 'XOM', 'GME', 'GLD', 'GS', 'HD', 'HON', 'INTC', 'IBM', 'JNJ', 'JPM', 'LIN', 'MRVL', 'MA', 'MCD', 'MDT', 'MRK', 'META', 'MSFT', 'MSTR', 'QQQ', 'NFLX', 'NVO', 'NVDA', 'ORCL', 'PLTR', 'PEP', 'PFE', 'PM', 'PG', 'HOOD', 'CRM', 'SPY', 'TSLA', 'TMO', 'TQQQ', 'UNH', 'VTI', 'V', 'WMT']

BATCH_SIZE = 60
DELAY = 65  # seconds (slightly more than 60 to be safe)

data = []

for i in range(0, len(SYMBOLS), BATCH_SIZE):
    batch = SYMBOLS[i:i+BATCH_SIZE]
    print(f"Processing batch {i//BATCH_SIZE + 1}: symbols {i+1} to {min(i+BATCH_SIZE, len(SYMBOLS))}")
    
    for symbol in batch:
        url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'
        response = requests.get(url)
        print(f"{symbol}: {response.status_code}")
        
        if response.status_code == 200:
            quote = response.json()
            quote['symbol'] = symbol
            quote['date'] = datetime.now().strftime('%Y-%m-%d')
            data.append(quote)
        else:
            print(f"Error for {symbol}: {response.text}")
    
    # Sleep between batches (except after the last batch)
    if i + BATCH_SIZE < len(SYMBOLS):
        print(f"Sleeping for {DELAY} seconds to respect rate limits...")
        time.sleep(DELAY)

print(f"Successfully fetched data for {len(data)} symbols")

with open('stock_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Saved all data to stock_data.json")








'''import requests
import json
from datetime import datetime

import os
API_KEY = os.environ.get("FINNHUB_API_KEY")
# API_KEY = "FINNHUB_API_KEY"
print(f"API_KEY used: {API_KEY}")
SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']  # Add all your symbols here

data = []
for symbol in SYMBOLS:
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'
    response = requests.get(url)
    print(f"{symbol}: {response.status_code} {response.text}")
    
    if response.status_code == 200:
        quote = response.json()
        quote['symbol'] = symbol
        quote['date'] = datetime.now().strftime('%Y-%m-%d')
        data.append(quote)

with open('stock_data.json', 'w') as f:
    json.dump(data, f)'''
