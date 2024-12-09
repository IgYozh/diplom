import asyncio
import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

async def find_primes_in_range(start, end):
    return [n for n in range(start, end) if is_prime(n)]

async def main():
    ranges = [(1, 500000), (500000, 1000000), (1000000, 5000000)]
    tasks = [find_primes_in_range(start, end) for start, end in ranges]
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    primes = [prime for sublist in results for prime in sublist]
    end_time = time.time()
    print(f"Found primes: {primes}")
    print(f"Asyncio took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
