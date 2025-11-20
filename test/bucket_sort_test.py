from algorithm.sort.bucket_sort import bucket_sort

import numpy as np
import unittest

class TestBucketSort(unittest.TestCase) :
    def test_positive_integer(self) -> None :
        for _ in range(1, 10) :
            arr = np.random.randint(1, 30, 10).tolist()
            sorted_arr = sorted(arr)
            bucket_sort(arr)
            self.assertListEqual(arr, sorted_arr)

    def test_negative_integer(self) -> None :
        for _ in range(1, 10) :
            arr = np.random.randint(-30, -1, 10).tolist()
            sorted_arr = sorted(arr)
            bucket_sort(arr)
            self.assertListEqual(arr, sorted_arr)
