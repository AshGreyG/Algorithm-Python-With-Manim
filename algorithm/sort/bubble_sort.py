from typing import TypeVar, List, Protocol, Self

class SupportsGreaterThan(Protocol) :
    def __gt__(self, other : Self) -> bool :
        ...

T = TypeVar("T", bound = SupportsGreaterThan)

def bubble_sort(array : List[T]) -> None :
    n = len(array)
    swapped = True
    while swapped :
        swapped = False
        for i in range(1, n) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

def memorized_bubble_sort(array : List[T]) -> None :
    j = len(array)
    swapped = True
    while swapped :
        swapped = False
        for i in range(1, j) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
                j = i
