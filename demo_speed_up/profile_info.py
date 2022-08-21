import gc
import os
import time
from functools import wraps

import psutil


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile_time_and_mem(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        mem_after = get_process_memory()
        print(
            f"Func: {func.__qualname__}. elapsed_time: {elapsed_time:.2f} second.")
        print(
            f"Mem diff: {(mem_after - mem_before)/2e6:.2f} MB. Mem before: {mem_before/2e6:.2f} MB, mem after: {mem_after/2e6:.2f} MB.")
        return result
    return wrapper
