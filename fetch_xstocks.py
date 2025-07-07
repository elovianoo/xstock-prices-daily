import requests
import json
from datetime import datetime

import os
API_KEY = os.environ.get('FINNHUB_API_KEY')
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
    json.dump(data, f)
