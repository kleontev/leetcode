# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
import unittest


def search(nums: List[int], target: int, first: bool) -> int:
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


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = search(nums, target, first=True)

        if first != -1:
            last = search(nums, target, first=False)
        else:
            last = -1

        return [first, last]


class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()

        tests = [
            ([2, 2, 2], 2, [0, 2]),
            ([2, 2], 2, [0, 1]),
            ([2, 2], 3, [-1, -1]),
            ([5, 7, 7, 8, 8, 10], 7, [1, 2]),
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 6, [-1, -1]),
        ]

        for nums, target, expectation in tests:
            with self.subTest(f"{nums}, {target}"):
                self.assertEqual(
                    solution.searchRange(nums, target),
                    expectation
                )
