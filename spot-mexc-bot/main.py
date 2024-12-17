import time
from mexc_api.spot import Spot
from mexc_api.websocket import SpotWebsocketStreamClient
from mexc_api.common.enums import Side, OrderType, StreamInterval, Action
from mexc_api.common.exceptions import MexcAPIError

KEY = "mx0vglYTp5kZz5o6kS"
SECRET = "d0ab0da7ef3d491f9610de75d015d48e"

spot = Spot(KEY, SECRET)

trading_pairs = ["MXUSDT", "OPUSDT"]

print("Доступные торговые пары:")
for index, pair in enumerate(trading_pairs, start=1):
    print(f"{index}. {pair}")

pair_choice = input("Выберите номер торговой пары: ").strip()
try:
    pair_index = int(pair_choice) - 1
    if pair_index < 0 or pair_index >= len(trading_pairs):
        raise ValueError("Неверный индекс.")
    trading_pair = trading_pairs[pair_index]
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите номер из списка.")
    exit()


action = input("Вы хотите (1) купить или (2) продать? Введите 1 или 2: ").strip()

if action == "1":
    order_type = input("Введите тип ордера (LIMIT или MARKET) для покупки: ").strip().upper()

    if order_type == "LIMIT":
        price = input("Введите цену для лимитного ордера: ")
        quantity = input("Введите количество для лимитного ордера: ")
        order = spot.account.new_order(
            trading_pair,
            Side.BUY,
            OrderType.LIMIT,
            quantity,
            price=price
        )
    elif order_type == "MARKET":
        quantity = input("Введите количество для маркет-ордера: ")
        order = spot.account.new_order(
            trading_pair,
            Side.BUY,
            OrderType.MARKET,
            quantity
        )
    else:
        print("Неверный тип ордера. Пожалуйста, введите LIMIT или MARKET.")
        exit()

elif action == "2":
    sell_order_type = input("Введите тип ордера (LIMIT или MARKET) для продажи: ").strip().upper()

    if sell_order_type == "LIMIT":
        price = input("Введите цену для лимитного ордера на продажу: ")
        quantity = input("Введите количество для лимитного ордера на продажу: ")
        sell_order = spot.account.new_order(
            trading_pair,
            Side.SELL,
            OrderType.LIMIT,
            quantity,
            price=price
        )
    elif sell_order_type == "MARKET":
        quantity = input("Введите количество для маркет-ордера на продажу: ")
        sell_order = spot.account.new_order(
            trading_pair,
            Side.SELL,
            OrderType.MARKET,
            quantity
        )
    else:
        print("Неверный тип ордера. Пожалуйста, введите LIMIT или MARKET.")
        exit()

else:
    print("Неверный выбор. Пожалуйста, введите 1 для покупки или 2 для продажи.")
    exit()

print("Ордер успешно размещен!")