from algorithm.sort.insertion_sort import insertion_sort
from typing import List

def bucket_sort(array : List[int]) -> None :
    min_val = min(array)
    max_val = max(array)
    bucket_count = len(array)
    bucket_size = max((max_val - min_val + 1) // bucket_count, 1);
    buckets : List[List[int]] = [[] for _ in range(bucket_count)]

    for num in array :
        bucket_index = int((num - min_val) / bucket_size)
        bucket_index = min(bucket_index, bucket_count - 1)
        buckets[bucket_index].append(num)

    sorted_array = []
    for bucket in buckets :
        if bucket :
            insertion_sort(bucket)
            sorted_array.extend(bucket)

    for i in range(len(array)) :
        array[i] = sorted_array[i]
