# Ref: https://stackoverflow.com/questions/21159103/what-kind-of-problems-if-any-would-there-be-combining-asyncio-with-multiproces
import asyncio
import gc
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pandas as pd

from profile_info import profile_time_and_mem


def blocking_func(x):
    time.sleep(x)  # Pretend this is expensive calculations
    return x * 5


@profile_time_and_mem
def some_func(x=2000000000):
    gc.collect()
    df = pd.DataFrame(np.arange(x), columns=['old'])
    sum = df.sum()
    print(df.iloc[-3:])
    return sum


@asyncio.coroutine
def run_execute(loop):
    #pool = multiprocessing.Pool()
    # out = pool.apply(blocking_func, args=(10,)) # This blocks the event loop.
    executor = ProcessPoolExecutor()
    # This does not
    # out = yield from loop.run_in_executor(executor, blocking_func, 5)
    out = yield from loop.run_in_executor(executor, some_func)
    return out


def go_loop():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_execute(loop))


if __name__ == "__main__":
    go_loop()
    some_func()
