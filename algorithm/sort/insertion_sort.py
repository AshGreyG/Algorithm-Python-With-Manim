from typing import TypeVar, List, Protocol, Self

class SupportsGreaterThan(Protocol) :
    def __gt__(self, other : Self) -> bool :
        ...

T = TypeVar("T", bound = SupportsGreaterThan)

def insertion_sort(array : List[T]) -> None :
    i = 1
    while i < len(array) :
        j = i
        while j > 0 and array[j - 1] > array[j] :
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1
