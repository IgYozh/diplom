import threading
import yfinance as yf
import time


# Функция для получения исторических данных для одной акции
def fetch_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="1y")  # Загружаем данные за год
    print(f"Data for {stock_symbol}:")
    print(data.head())  # Печатаем первые 5 строк данных


# Основная функция, которая будет запускать потоки для всех акций
def main():
    stock_symbols = ["AAPL", "MSFT", "GOOG", "AMZN"]  # Список символов акций

    # Список для потоков
    threads = []

    # Создаём поток для каждой акции
    for symbol in stock_symbols:
        thread = threading.Thread(target=fetch_stock_data, args=(symbol,))
        threads.append(thread)
        thread.start()  # Запускаем поток

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()  # Ждём завершения каждого потока


# Запускаем программу
if __name__ == "__main__":
    start_time = time.time()  # Засекаем время начала
    main()  # Запускаем основную программу
    end_time = time.time()  # Засекаем время завершения
    print(f"\nИтоговое время выполнения: {end_time - start_time:.2f} секунд")  # Выводим время выполнения
