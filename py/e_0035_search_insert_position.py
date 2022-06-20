# https://leetcode.com/problems/search-insert-position
from typing import List
import unittest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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

        return left


class TestSolution(unittest.TestCase):
    def test_search_insert(self):
        solution = Solution()

        tests = [
            ([], 100, 0),
            ([1], 100, 1),
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
        ]

        for nums, target, expectation in tests:
            with self.subTest(f"{nums}, {target}"):
                self.assertEqual(
                    solution.searchInsert(nums, target),
                    expectation
                )
