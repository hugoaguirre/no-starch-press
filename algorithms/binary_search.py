"""
    Binary search implementation

    Returns element index when found, None when not found
"""
from typing import List

def binary_search(num: int, sorted_nums: List[int]):
    low = 0
    high = len(sorted_nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] == num:
            return mid

        if num > sorted_nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == "__main__":
   print(binary_search(7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
   print(binary_search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
   print(binary_search(42, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
