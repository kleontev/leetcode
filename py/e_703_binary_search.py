from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                return mid

        return -1


class TestSolution(unittest.TestCase):
    def test_search(self):
        solution = Solution()

        tests = [
            ([], 100, -1),
            ([1], 100, -1),
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
        ]

        for nums, target, expectation in tests:
            with self.subTest(f"{nums}, {target}"):
                self.assertEqual(
                    solution.search(nums, target),
                    expectation
                )
