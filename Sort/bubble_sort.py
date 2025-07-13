from typing import TypeVar, List, NoReturn

T = TypeVar("T")

def bubble_sort(array : List[T]) -> NoReturn :
    n = len(array)
    swapped = True
    while swapped == True :
        swapped = False
        for i in range(1, n) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

def memorized_bubble_sort(array : List[T]) -> NoReturn :
    n = len(array)
    j = len(array)
    swapped = True
    while swapped == True :
        swapped = False
        for i in range(1, j) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
                j = i