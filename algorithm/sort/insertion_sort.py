from typing import List

def insertion_sort(array : List[int]) -> None :
    i = 1
    while i < len(array) :
        j = i
        while j > 0 and array[j - 1] > array[j] :
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1
