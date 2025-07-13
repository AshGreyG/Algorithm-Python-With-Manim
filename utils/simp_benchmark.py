from typing import Callable, TypeVar, Any, NoReturn
from time import perf_counter

Func = TypeVar("Func", bound = Callable[..., Any])

def function_timer(func : Func) -> NoReturn :
    def wrapper(*args : Any, **kwargs : Any) -> float :
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        return (end - start) * 1000 * 1000
    return wrapper