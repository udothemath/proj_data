import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

from profile_info import profile_time_and_mem


def blocking_func(x):
    time.sleep(x)  # Pretend this is expensive calculations
    return x * 5


@asyncio.coroutine
def run_execute(loop):
    #pool = multiprocessing.Pool()
    # out = pool.apply(blocking_func, args=(10,)) # This blocks the event loop.
    executor = ProcessPoolExecutor()
    # This does not
    out = yield from loop.run_in_executor(executor, blocking_func, 2)
    print(out)


@profile_time_and_mem
def go_loop():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_execute(loop))


if __name__ == "__main__":
    go_loop()
