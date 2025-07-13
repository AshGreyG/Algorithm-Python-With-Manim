from .bubble_sort import bubble_sort, memorized_bubble_sort
from typing import NoReturn

import numpy as np
import unittest

class TestBubbleSort(unittest.TestCase) :
    def test_positive_integer(self) -> NoReturn :
        for i in range(1, 10) :
            arr = np.random.randint(1, 30, 10).tolist()
            sorted_arr = sorted(arr)
            bubble_sort(arr)
            self.assertListEqual(arr, sorted_arr)

    def test_negative_integer(self) -> NoReturn :
        for i in range(1, 10) :
            arr = np.random.randint(-30, -1, 10).tolist()
            sorted_arr = sorted(arr)
            bubble_sort(arr)
            self.assertListEqual(arr, sorted_arr)

class TestMemorizedBubbleSort(unittest.TestCase) :
    def test_positive_integer(self) -> NoReturn :
        for i in range(1, 10) :
            arr = np.random.randint(1, 30, 10).tolist()
            sorted_arr = sorted(arr)
            memorized_bubble_sort(arr)
            self.assertListEqual(arr, sorted_arr)

    def test_negative_integer(self) -> NoReturn :
        for i in range(1, 10) :
            arr = np.random.randint(-30, -1, 10).tolist()
            sorted_arr = sorted(arr)
            memorized_bubble_sort(arr)
            self.assertListEqual(arr, sorted_arr)