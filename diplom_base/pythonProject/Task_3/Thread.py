import threading
import requests
import time

def download_file(url, file_name):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"{file_name} скачан!")
        else:
            print(f"Ошибка при скачивании {file_name}: {response.status_code}")
    except Exception as e:
        print(f"Ошибка {file_name}: {e}")

def download_with_threading(urls):
    threads = []
    for i, url in enumerate(urls):
        file_name = f"financial_data_{i + 1}.csv"  # Название файла
        thread = threading.Thread(target=download_file, args=(url, file_name))
        threads.append(thread)
        thread.start()

    # Ждём завершения всех потоков
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()

    urls = [
        "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv",
    ]

    print("Скачивание с использованием Threading...")
    download_with_threading(urls)

    print(f"Итоговое время выполнения: {time.time() - start_time:.2f} секунд")
