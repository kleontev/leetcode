import math
from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = 0
        max_subarray = -math.inf
        
        for n in nums:
            current_subarray += n
            max_subarray = max(current_subarray, max_subarray)
            
            if current_subarray < 0:
                current_subarray = 0

        return max_subarray


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            ([-1, 1000, -1, -1, -1, 1000, -1], 1000 * 2 - 3),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([5, 4, -1, 7, 8], 23),
            ([1], 1)
        ]

        for test, expectation in tests:
            with self.subTest(
                f'test={test}'
                f'expectation={expectation}'
            ):
                self.assertEqual(
                    solution.maxSubArray(test),
                    expectation
                )
