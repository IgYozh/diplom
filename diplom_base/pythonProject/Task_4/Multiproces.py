from concurrent.futures import ProcessPoolExecutor
import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    return [n for n in range(start, end) if is_prime(n)]

def process_range(r):
    return find_primes_in_range(r[0], r[1])

def main():
    ranges = [(1, 500000), (500000, 1000000), (1000000, 5000000)]
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_range, ranges))  # Используем обычную функцию
    primes = [prime for sublist in results for prime in sublist]
    end_time = time.time()
    print(f"Found primes: {primes}")
    print(f"Multiprocessing took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
