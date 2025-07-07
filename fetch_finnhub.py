import requests

API_KEY = "d1lv271r01qksvur9ukgd1lv271r01qksvur9ul0"
SYMBOL = "AAPL"
url = f"https://finnhub.io/api/v1/quote?symbol={SYMBOL}&token={API_KEY}"

response = requests.get(url)
print(response.json())

with open('stock_data2.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Saved Finnhub response to stock_data.json")
