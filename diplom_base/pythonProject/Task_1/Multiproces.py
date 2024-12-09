import requests
from multiprocessing import Pool
import time

def fetch_currency_rate(args):
    base_currency, target_currency, api_key, amount = args
    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}&access_key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if not data.get("success", True):
            print(f"API Error: {data.get('error', {}).get('info', 'Unknown error')}")
            return None
        return data.get('result')
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {base_currency} -> {target_currency}: {e}")
        return None

def main_multiprocessing():
    base_currency = "USD"  # Базовая валюта — рубль
    target_currencies = ['EUR', 'RUB', 'GBP', 'JPY']  # Валюты для конверсии
    api_key = "bb4110e63f7d8041b0ab51d7ae123aaa"  # Свой API-ключ
    amount = 1  # Конвертируем 1 доллар

    tasks = [(base_currency, target, api_key, amount) for target in target_currencies]

    start_time = time.time()  # Засекаем время начала

    with Pool(processes=4) as pool:
        results = pool.map(fetch_currency_rate, tasks)

    end_time = time.time()  # Засекаем время завершения

    # Вывод результатов
    for currency, rate in zip(target_currencies, results):
        if rate is None:
            print(f"{base_currency} -> {currency}: Error fetching rate")
        else:
            print(f"{amount} {base_currency} -> {currency}: {rate:.2f}")

    print(f"\nИтоговое значение времени: {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    main_multiprocessing()
