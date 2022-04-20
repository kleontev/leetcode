# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List
import unittest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # trivial O(N log N)
        return sorted(n * n for n in nums)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
        ]

        for nums, expectation in tests:
            with self.subTest(f"{nums}"):
                self.assertEqual(
                    solution.sortedSquares(nums),
                    expectation
                )
