import requests

def get_wallet_balance(wallet_address):
    url = "https://api.mainnet-beta.solana.com"
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [
            wallet_address,
            {"commitment": "confirmed"}
        ]
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        print("Ответ API:", data)

        if 'result' in data:
            balance = data['result']['value']
            print(f"Баланс кошелька {wallet_address}: {balance / 1_000_000_000} SOL")
        else:
            print("Ошибка в ответе API:", data.get('error', 'Неизвестная ошибка'))
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")

wallet_address = input("Введите адрес кошелька: ")
get_wallet_balance(wallet_address)