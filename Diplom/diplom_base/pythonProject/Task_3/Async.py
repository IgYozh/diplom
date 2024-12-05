import aiohttp
import asyncio
import time

async def download_file_async(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(file_name, "wb") as file:
                    file.write(await response.read())
                print(f"{file_name} скачан!")
            else:
                print(f"Ошибка при скачивании {file_name}: {response.status}")

async def download_with_asyncio(urls):
    tasks = []
    for i, url in enumerate(urls):
        file_name = f"file_{i + 1}.csv"
        tasks.append(download_file_async(url, file_name))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()

    urls = [
        "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv",
        "https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_male.csv",
    ]

    print("Скачивание с использованием Asyncio...")
    asyncio.run(download_with_asyncio(urls))

    print(f"Итоговое время выполнения: {time.time() - start_time:.2f} секунд")
