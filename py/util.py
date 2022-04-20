from typing import List


def binary_search(nums: List[int], target: int, first: bool = True) -> int:
    result = -1

    if not nums:
        return result

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            if first:
                right = mid - 1
            else:
                left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return result
