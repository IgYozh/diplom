import asyncio
import aiohttp
import time

async def fetch_currency_rate(session, base_currency, target_currency, api_key, amount=1):
    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}&access_key={api_key}"
    async with session.get(url) as response:
        data = await response.json()
        if not data.get("success", True):
            print(f"API Error: {data.get('error', {}).get('info', 'Unknown error')}")
            return None
        return data.get('result')


async def main_async():
    base_currency = "USD"
    target_currencies = ['EUR', 'RUB', 'GBP', 'JPY']
    api_key = "bb4110e63f7d8041b0ab51d7ae123aaa"  # Свой API-ключ
    amount = 1  # Конвертируем 1 USD

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_currency_rate(session, base_currency, target, api_key, amount) for target in target_currencies]
        results = await asyncio.gather(*tasks)

    for currency, rate in zip(target_currencies, results):
        if rate is None:
            print(f"{base_currency} -> {currency}: Error fetching rate")
        else:
            print(f"{amount} {base_currency} -> {currency}: {rate:.2f}")



if __name__ == "__main__":
    start_time = time.time()  # Засекаем стартовое время
    asyncio.run(main_async())  # Запускаем асинхронный код
    end_time = time.time()  # Засекаем время завершения

    print(f"\nИтоговое время выполнения: {end_time - start_time:.2f} секунд")  # Выводим разницу