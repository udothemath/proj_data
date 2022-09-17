import logging
import time
from datetime import datetime
from functools import wraps
import os
import psutil

# Memory from: https://stackoverflow.com/questions/552744/how-do-i-profile-memory-usage-in-python
# Example from: https://www.geeksforgeeks.org/create-an-exception-logging-decorator-in-python/


def elapsed_since(start: time.time()):
    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def dec_profile(logger=logging.getLogger(__name__)):
    def profile(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mem_before = get_process_memory()
            start = time.time()
            result = func(*args, **kwargs)
            elapsed_time = elapsed_since(start)
            mem_after = get_process_memory()
            # str(round(bytes / 1e6, 2)
            log_dict = {
                "Elapsed time": f"{elapsed_time}",
                "Memory usage": f"{str(round((mem_after - mem_before) / 1e6, 2))} MB",
                "Memory before": f"{str(round((mem_before) / 1e6, 2))} MB",
                "Memory after": f"{str(round((mem_after) / 1e6, 2))} MB",
            }
            logger.info(log_dict)
            # logger.info("{}: memory before: {:,}, after: {:,}, consumed: {:,}; exec time: {}".format(
            #     func.__name__,
            #     mem_before, mem_after, mem_after - mem_before,
            #     elapsed_time))
            return result
        return wrapper
    return profile


def create_logger(log_filename: str = f'exc_logger_{datetime.now():%Y_%m_%d}.log'):

    # create a logger object
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)

    # c reate a file to store all the
    # logged exceptions
    logfile = logging.FileHandler(log_filename)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)

    logfile.setFormatter(formatter)
    logger.addHandler(logfile)

    return logger

# logger = create_logger()

# # you will find a log file
# # created in a given path
# print(logger)


def dec_exception(logger=logging.getLogger(__name__)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                issue = "exception in "+func.__name__+"\n"
                issue = issue+"=============\n"
                logger.exception(issue)
                raise
        return wrapper
    return decorator


def dec_calc_time(logger=logging.getLogger(__name__)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start = time.perf_counter()
                a = func(*args, **kwargs)
                elapsed_time = time.perf_counter() - start
                log_info = {'Func name': func.__qualname__,
                            'Elapsed time': f'{elapsed_time:.2f}'}
                logger.info(log_info)
                return a
            except:
                issue = f'Func name: {func.__qualname__} \n'
                issue = issue+"=============\n"
                logger.exception(issue)
                raise
        return wrapper
    return decorator

# @exception(logger)
# def divideByZero():
# 	return 12/0

# # Driver Code
# if __name__ == '__main__':
# 	divideByZero()
