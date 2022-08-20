import os
import time
from functools import lru_cache

from memory_profiler import memory_usage, profile

log_file = open('profile.log', 'w+')


@profile(stream=log_file)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


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
    start = time.perf_counter()
    # main(func=fib_cache, n_size=100)

    my_func()

    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.2f} second.")
