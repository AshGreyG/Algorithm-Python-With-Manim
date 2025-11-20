from typing import Callable, TypeVar, Any
from time import perf_counter

import functools
import tracemalloc

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

def function_memory_monitor():
    def decorator(func: Callable[..., Any]) -> Callable[..., int]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> int:
            tracemalloc.start()
            _ = func(*args, **kwargs)
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return peak
        return wrapper
    return decorator
