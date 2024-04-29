import requests
import pandas as pd


def get_historical_btc_price():
    URL = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=500"
    response = requests.get(URL)
    data = response.json()
    prices = [float(item[4]) for item in data]  # 4. eleman "Kapanış" fiyatı
    return prices


def calculate_moving_average(prices):
    df = pd.DataFrame(prices, columns=['Price'])
    df['MA_200'] = df['Price'].rolling(window=200).mean()  # 200 günlük hareketli ortalama hesaplanıyor
    return df['MA_200'].values


prices = get_historical_btc_price()
ma_prices = calculate_moving_average(prices)

# Son günün kapanış fiyatı ve hareketli ortalaması
last_price = prices[-1]
last_ma = ma_prices[-1]
print("Price: {0}, Moving Average: {1}".format(last_price, last_ma))

# Son fiyatın hareketli ortalamanın üzerinde olup olmadığını kontrol
if last_price > last_ma:
    print("Son fiyat, 200 günlük hareketli ortalamanın üzerinde.")
else:
    print("Son fiyat, 200 günlük hareketli ortalamanın altında.")