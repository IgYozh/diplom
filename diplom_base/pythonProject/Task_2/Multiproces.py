import multiprocessing
import yfinance as yf
import time


# Функция для получения исторических данных для одной акции
def fetch_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    data = stock.history(period="1y")  # Загружаем данные за год
    print(f"Data for {stock_symbol}:")
    print(data.head())  # Печатаем первые 5 строк данных


# Основная функция, которая будет запускать процессы для всех акций
def main():
    stock_symbols = ["AAPL", "MSFT", "GOOG", "AMZN"]  # Список символов акций

    # Создаём процессы для каждой акции
    processes = []

    # Создаём процесс для каждой акции
    for symbol in stock_symbols:
        process = multiprocessing.Process(target=fetch_stock_data, args=(symbol,))
        processes.append(process)
        process.start()  # Запускаем процесс

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()  # Ждём завершения каждого процесса


# Запускаем программу
if __name__ == "__main__":
    start_time = time.time()  # Засекаем время начала
    main()  # Запускаем основную программу
    end_time = time.time()  # Засекаем время завершения
    print(f"\nExecution time: {end_time - start_time:.2f} seconds")  # Выводим время выполнения
