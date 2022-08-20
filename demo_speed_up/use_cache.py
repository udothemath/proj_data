import os
import time
from functools import lru_cache


@lru_cache(maxsize=16)
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main(func, n_size=30):
    for i in range(n_size+1):
        print(i, func(i))
    print("done")


if __name__ == '__main__':
    # start = time.perf_counter()
    # main(func=fib_cache, n_size=100)
    # elapsed = time.perf_counter() - start
    # print(f"Elapsed: {elapsed:.2f} second.")
