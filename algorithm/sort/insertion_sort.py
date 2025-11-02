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

def binary_insertion_sort(array : List[T]) -> None :
    i = 1
    while i < len(array) :
        lf = 0
        rt = i - 1
        pos = lf
        while lf <= rt :
            mid = (lf + rt) // 2
            if array[mid] == array[i] :
                pos = mid
                break
            elif array[mid] < array[i] :
                lf = mid + 1
            else :
                rt = mid - 1
            pos = lf
        temp = array[i]
        for j in range(i - 1, pos - 1, -1) :
            array[j + 1] = array[j]
        array[pos] = temp
        i += 1
