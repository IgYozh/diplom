import asyncio
import yfinance as yf
import time


# Асинхронная функция для получения исторических данных
async def fetch_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="1y")  # Загружаем данные за год
    return stock_symbol, data  # Возвращаем символ акции и её данные


# Основная асинхронная функция, которая будет запускать запросы для всех акций
async def main():
    stock_symbols = ["AAPL", "MSFT", "GOOG", "AMZN"]  # Список символов акций

    # Создаём задачи для каждой акции
    tasks = [fetch_stock_data(symbol) for symbol in stock_symbols]

    # Параллельно запускаем все задачи
    results = await asyncio.gather(*tasks)

    # Выводим данные для каждой акции
    for symbol, data in results:
        print(f"Data for {symbol}:")
        print(data.head())  # Печатаем первые 5 строк данных


# Запускаем основной процесс
if __name__ == "__main__":
    start_time = time.time()  # Засекаем время начала
    asyncio.run(main())  # Запускаем асинхронную программу
    end_time = time.time()  # Засекаем время завершения
    print(f"\nИтоговое время выполнения: {end_time - start_time:.2f} секунд")  # Выводим время выполнения
