import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

#Выполняет HTTP-запрос для получения курса валют и Обрабатывает ошибки, если запрос не удался
def fetch_currency_rate(base_currency, target_currency, api_key, amount=1):
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


def main_threading():
    base_currency = "USD"  # Базовая валюта — доллар
    target_currencies = ['EUR', 'RUB', 'GBP', 'JPY']  # Валюты для конверсии
    api_key = "bb4110e63f7d8041b0ab51d7ae123aaa"  # Замени на свой API-ключ
    amount = 1 # Конвертируем 1 доллар

    tasks = []
    results = []

    start_time = time.time()  # Засекаем время начала
    # #Создаёт пул потоков, где каждая задача обрабатывается независимо
    with ThreadPoolExecutor(max_workers=4) as executor:
        for target in target_currencies:
            tasks.append(
                executor.submit(fetch_currency_rate, base_currency, target, api_key, amount)
            )

        for future in as_completed(tasks): #as_completed для обработки задач по мере их завершения.
            results.append(future.result())

    end_time = time.time()  # Засекаем время завершения

    # Вывод результатов
    for currency, rate in zip(target_currencies, results):
        if rate is None:
            print(f"{base_currency} -> {currency}: Error fetching rate")
        else:
            print(f"{amount} {base_currency} -> {currency}: {rate:.2f}")

    print(f"\nИтоговое время выполнения: {end_time - start_time:.2f} секунд")


if __name__ == "__main__":
    main_threading()
