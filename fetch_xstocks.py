import finnhub
import json
import os
from datetime import datetime

print("Script started")

# API_KEY = os.environ.get('FINNHUB_API_KEY')
API_KEY = d1lra9hr01qt4thi06tgd1lra9hr01qt4thi06u0
# print(f"API_KEY loaded: {API_KEY is not None}")

# Create Finnhub client
finnhub_client = finnhub.Client(api_key=API_KEY)

SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']

data = []
for symbol in SYMBOLS:
    try:
        print(f"Fetching {symbol}...")
        quote = finnhub_client.quote(symbol)
        quote['symbol'] = symbol
        quote['date'] = datetime.now().strftime('%Y-%m-%d')
        data.append(quote)
        print(f"{symbol}: Success")
    except Exception as e:
        print(f"{symbol}: Error - {e}")

print(f"Total data collected: {len(data)}")
with open('stock_data.json', 'w') as f:
    json.dump(data, f)
print("Script completed")


'''import requests
import json
from datetime import datetime

# import os
# API_KEY = os.environ.get(FINNHUB_API_KEY)
API_KEY = 'YOUR_FINNHUB_API_KEY'
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
