import os
import sys
import time
from functools import lru_cache, wraps

from memory_profiler import LogFile, memory_usage, profile


# sys.stdout = LogFile('memory_profile_log', reportIncrementFlag=False)
def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"func: {func.__qualname__}. Elapsed: {elapsed:.2f} second.")
        return result
    return wrapper


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


@get_time
@profile(stream=log_file)
def main(func, n_size=30):
    for i in range(n_size+1):
        print(i, func(i))
    print("done")


if __name__ == '__main__':
    main(func=fib, n_size=20)
    main(func=fib_cache, n_size=200)
