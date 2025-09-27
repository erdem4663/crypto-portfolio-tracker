import requests

PORTFOLIO = {"bitcoin": 0.5, "ethereum": 2}

def get_price(symbol):
    url = "https://api.coingecko.com/api/v3/simple/price"
    r = requests.get(url, params={"ids": symbol, "vs_currencies": "usd"})
    r.raise_for_status()
    data = r.json()
    return data[symbol]["usd"]

if __name__ == "__main__":
    total_value = 0
    for coin, amount in PORTFOLIO.items():
        price = get_price(coin)
        value = price * amount
        print(f"{coin}: {amount} coins × ${price} = ${value}")
        total_value += value
    print("Total Portfolio Value: $", total_value)
