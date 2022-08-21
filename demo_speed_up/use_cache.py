# %%
import asyncio
import gc
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache, wraps
from time import sleep

import numpy as np
import pandas as pd
import psutil
from IPython.display import display
from memory_profiler import LogFile, memory_usage, profile
from tqdm import tqdm

from profile_info import profile_time_and_mem

log_file = open('profile.log', 'w+')
# sys.stdout = LogFile('memory_profile_log', reportIncrementFlag=False)


def info_bar():
    ''' memory usage status report bar '''
    with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
        while True:
            rambar.n = psutil.virtual_memory().percent
            cpubar.n = psutil.cpu_percent()
            rambar.refresh()
            cpubar.refresh()
            sleep(0.5)


def get_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"func: {func.__qualname__}. elapsed_time: {elapsed:.2f} second.")
        return result
    return wrapper


@profile(stream=log_file)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


@profile(stream=log_file)
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
def main(func, n_size=30):
    for i in range(n_size+1):
        print(i, func(i))
    print("done")


# @get_time
# @profile(stream=log_file)
@profile_time_and_mem
def df_concat_once():
    gc.collect()
    df = pd.DataFrame(np.random.randn(10000000, 4), columns=list('ABCD'))
    n_partitions = 4
    dfs = np.array_split(df, n_partitions)
    for i in range(n_partitions):
        dfs[i]['E'] = dfs[i]['A'] * 1000 + dfs[i]['B'] * 10
    df_result = pd.concat(dfs)
    print(f'{"="*20}')
    print(f"df size: {df.shape}. df_result size: {df_result.shape}")
    print(df.iloc[[0, -1], :])
    print(df_result.iloc[[0, -1], :])
    print(f'{"="*20}')
    print('done')
    del df, df_result
    gc.collect()


@profile_time_and_mem
def df_concat_incremental():
    gc.collect()
    df = pd.DataFrame(np.random.randn(10000000, 4), columns=list('ABCD'))
    n_partitions = 4
    df_result = pd.DataFrame()
    dfs = np.array_split(df, n_partitions)
    for curr_df in dfs:
        curr_df['E'] = curr_df['A'] * 1000 + curr_df['B'] * 10
        if curr_df is dfs[0]:
            df_result = curr_df
        else:
            df_result = pd.concat([df_result, curr_df])
        del curr_df
    print(f'{"="*20}')
    print(f"df size: {df.shape}. df_result size: {df_result.shape}")
    print(df.iloc[[0, -1], :])
    print(df_result.iloc[[0, -1], :])
    print(f'{"="*20}')
    print('done')


if __name__ == '__main__':
    df_concat_once()
    df_concat_incremental()

    # main(func=fib, n_size=20)
    # main(func=fib_cache, n_size=200)
