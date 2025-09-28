from typing import Callable, TypeVar, Any, cast
from time import perf_counter, sleep

import os
import functools
import psutil
import threading

T = TypeVar("T")

def function_timer(func : Callable[..., Any]) -> Callable[..., float] :
    """
    This is a decorator function to get the execution time of the
    wrapped function. Unit in ns.
    """

    def wrapper(*args : Any, **kwargs : Any) -> float :
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        return (end - start) * 1000 * 1000
    return wrapper

def function_memory_monitor(interval : float = 0.01) :
    def decorator(func : Callable[..., Any]) -> Callable[..., int] :
        @functools.wraps(func)
        def wrapper(*args : Any, **kwargs : Any) -> int :
            # Get current thread
            process = psutil.Process(os.getpid())

            max_peak : int = process.memory_info().rss
            start_memory : int = process.memory_info().rss

            def monitor() -> None :
                nonlocal max_peak
                while not cast(bool, monitor.stop) : # type: ignore[attr-defined]
                    current_memory = process.memory_info().rss
                    if current_memory > max_peak :
                        max_peak = current_memory

                    sleep(interval)

            monitor.stop = False # type: ignore[attr-defined]
            thread = threading.Thread(target = monitor)
            thread.start()

            try :
                _ = func(*args, **kwargs)
            finally :
                monitor.stop = True # type: ignore[attr-defined]
                thread.join(timeout = 1)

            peek_diff = max_peak - start_memory

            return peek_diff
        return wrapper
    return decorator
