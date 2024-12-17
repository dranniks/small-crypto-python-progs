import requests

def get_available_pairs():
    url = 'https://www.mexc.com/open/api/v2/market/symbols'
    response = requests.get(url)
    data = response.json()
    
    if 'data' in data:
        return [symbol['symbol'] for symbol in data['data']]
    else:
        raise ValueError("Не удалось получить список доступных торговых пар.")

def main():
    try:
        pairs = get_available_pairs()
        print("пары на MEXC:")
        for pair in pairs:
            
            if pair == 'BTC_USDT': print(pair)
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
