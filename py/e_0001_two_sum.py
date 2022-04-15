from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, v in enumerate(nums):
            c = target - v
            if c in diff:
                return [diff[c], i]
            diff[v] = i


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1])
        ]

        for nums, target, expectation in tests:
            with self.subTest(f"{nums}"):
                self.assertEqual(
                    solution.twoSum(nums, target),
                    expectation
                )
