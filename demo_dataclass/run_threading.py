import time
import queue
import os
import threading
print('Hello')


source = ["eat", "sleep", "exercise", "code", "walk", "relax"]

threads_num = 4


def log(msg: str) -> None:
    pid = os.getpid()
    tid = threading.current_thread().ident
    print(f"process:[{pid}]. thread:[{tid}]{msg}")


def worker(q: queue):
    while True:
        item = q.get(block=True, timeout=2)
        if item == "STOP":
            log("Stop the thread")
            break
        log(f"Working on {item}")
        time.sleep(1)
        q.task_done()


def main():
    q = queue.Queue()
    for item in source:
        q.put(item)
    print(f"{'-'*20}")
    print(list(q.queue))
    print(f"{'-'*20}")

    threads = []
    for _ in range(threads_num):
        t = threading.Thread(target=worker, args=(q,))
        t.start()
        threads.append(t)
    q.join()

    for _ in range(threads_num):
        q.put("STOP")

    for t in threads:
        t.join()
    print('Done')


def test_time():
    start = time.perf_counter()
    time.sleep(2)
    elapsed_time = time.perf_counter() - start
    print(f"elapsed time: {elapsed_time:.3f}")


if __name__ == "__main__":
    # main()
    test_time()
