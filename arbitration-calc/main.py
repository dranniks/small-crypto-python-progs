import requests

def get_price_mexc(symbol):
    url = f'https://www.mexc.com/open/api/v2/market/ticker?symbol={symbol}'
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ValueError(f"Ошибка при запросе к MEXC: {response.status_code}")

    data = response.json()
    print("Ответ от MEXC:", data)
    if 'data' in data and len(data['data']) > 0:
        return float(data['data'][0]['last'])
    else:
        raise ValueError("Не удалось получить данные о ценах с MEXC.")

def get_price_binance(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Ошибка при запросе к Binance: {response.status_code}")

    data = response.json()
    print("Ответ от Binance:", data)
    if 'price' in data:
        return float(data['price'])
    else:
        raise ValueError("Не удалось получить данные о ценах с Binance.")

def calculate_arbitrage_profit(buy_price, sell_price, amount):
    total_buy_cost = buy_price * amount
    total_sell_revenue = sell_price * amount
    profit = total_sell_revenue - total_buy_cost
    return profit

def main():
    trading_pairs = {
        'BTC/USDT': {
            'mexc': 'BTC_USDT',
            'binance': 'BTCUSDT'
        },
        'ETH/USDT': {
            'mexc': 'ETH_USDT',
            'binance': 'ETHUSDT'
        },
    }

    print("Доступные торговые пары:")
    for pair in trading_pairs.keys():
        print(pair)

    chosen_pair = input("Выберите торговую пару (например, BTC/USDT): ")

    if chosen_pair not in trading_pairs:
        print("Неверная торговая пара.")
        return

    symbol_mexc = trading_pairs[chosen_pair]['mexc']
    symbol_binance = trading_pairs[chosen_pair]['binance']

    try:
        buy_price_mexc = get_price_mexc(symbol_mexc)
        sell_price_binance = get_price_binance(symbol_binance)

        print(f"Цена покупки на MEXC: {buy_price_mexc:.2f} USDT")
        print(f"Цена продажи на Binance: {sell_price_binance:.2f} USDT")

        amount = float(input("Введите количество актива для торговли: "))

        profit = calculate_arbitrage_profit(buy_price_mexc, sell_price_binance, amount)

        if profit > 0:
            print(f"Потенциальная прибыль от арбитража: {profit:.2f} USDT")
        else:
            print("Арбитраж невыгоден.")
            
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
