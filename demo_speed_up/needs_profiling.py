import asyncio
import cProfile
import io
import os
import pstats
import re
import time
from functools import wraps
from itertools import count

import httpx
import requests


def count_https_in_web_pages():
    with open('top15USWebsites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    htmls = []
    for url in urls:
        htmls = htmls + [requests.get(url).text]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')
    time.sleep(2.0)
    print(f'count_https: {count_https}')
    print(f'count_http: {count_http}')
    print(f'ratio: {count_https/count_http:.3f}%')


async def better_count_https_in_web_pages():
    with open('top15USWebsites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url, follow_redirects=True) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    time.sleep(2.0)
    print('finished parsing')
    print(f'{count_https}')
    print(f'{count_http}')
    print(f'{count_https/count_http}')


def main_timeit():
    start = time.perf_counter()
    count_https_in_web_pages()
    elapsed = time.perf_counter() - start
    print(f'Job is done in {elapsed:.2f}s.')


def main():
    import cProfile
    import pstats

    # with cProfile.Profile() as pr:
    #     asyncio.run(better_count_https_in_web_pages())
    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(better_count_https_in_web_pages())
    pr.disable()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='needs_profiling.prof')
    generate_png()


def generate_png():
    bash_script = 'python3 -m gprof2dot -f pstats needs_profiling.prof | dot -T png -o needs_profiling.png'
    os.system(bash_script)


def profile_func(func):
    @wraps(func)
    def decorator_func(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        val = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.dump_stats(filename=os.path.join('.', 'a_profiling.prof'))
        return val
    return decorator_func


@profile_func
def take_a_break():
    print("hello")
    time.sleep(2.0)
    print("Woke up")


if __name__ == '__main__':
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"Elapsed time: {elapsed:.2f} second.")
    # main_timeit()
    # take_a_break()
