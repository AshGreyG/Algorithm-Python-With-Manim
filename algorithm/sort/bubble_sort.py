from typing import List

def bubble_sort(array : List[int]) -> None :
    n = len(array)
    swapped = True
    while swapped :
        swapped = False
        for i in range(1, n) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

def memorized_bubble_sort(array : List[int]) -> None :
    j = len(array)
    swapped = True
    while swapped :
        swapped = False
        for i in range(1, j) :
            if array[i - 1] > array[i] :
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
                j = i
