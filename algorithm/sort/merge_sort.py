from typing import List

import math

def merge_sort(array : List[int]) -> None :
    def merge(p : int, q : int, r : int) -> None :
        n1 = q - p + 1
        n2 = r - q
        left  : List[int] = [0] * (n1 + 1)
        right : List[int] = [0] * (n2 + 1)

        for i in range(n1) :
            left[i] = array[p + i]

        for i in range(n2) :
            right[i] = array[q + i + 1]

        left[n1]  = math.inf
        right[n2] = math.inf

        m = 0
        n = 0
        for k in range(p, r + 1) :
            if left[m] <= right[n] :
                array[k] = left[m]
                m += 1
            else :
                array[k] = right[n]
                n += 1

    def _merge_sort(p : int, r : int) -> None :
        if p < r :
            q = (p + r) // 2
            _merge_sort(p, q)
            _merge_sort(q + 1, r)
            merge(p, q, r)

    _merge_sort(0, len(array) - 1)