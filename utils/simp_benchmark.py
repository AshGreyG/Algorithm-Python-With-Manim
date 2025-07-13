from typing import Callable, TypeVar, Any, NoReturn, List
from time import perf_counter, sleep

import os
import functools
import tracemalloc
import psutil
import threading

T = TypeVar("T")
Func = TypeVar("Func", bound = Callable[..., Any])

def function_timer(func : Func) -> Func :
    """
    This is a decorator function to get the execution time of the
    wrapped function. Unit in ns.
    """

    def wrapper(*args : Any, **kwargs : Any) -> float :
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        return (end - start) * 1000 * 1000
    return wrapper

def function_memory_monitor(interval : float = 0.01) :
    def decorator(func : Func) -> Func :
        @functools.wraps(func)
        def wrapper(*args : Any, **kwargs : Any) -> int :
            # Get current thread
            process = psutil.Process(os.getpid())

            max_peak = process.memory_info().rss
            start_memory = process.memory_info().rss
            end_memory = None

            def monitor() :
                nonlocal max_peak
                while not monitor.stop : 
                    current_memory = process.memory_info().rss
                    if current_memory > max_peak :
                        max_peak = current_memory

                    sleep(interval)

            monitor.stop = False
            thread = threading.Thread(target = monitor)
            thread.start()

            try :
                result = func(*args, **kwargs)
            finally :
                monitor.stop = True
                thread.join(timeout = 1)
                end_memory = process.memory_info().rss

            peek_diff = max_peak - start_memory
            end_diff = end_memory - start_memory

            return peek_diff
        return wrapper
    return decorator