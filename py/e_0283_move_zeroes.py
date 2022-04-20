from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        current = last_non_zero = 0

        while current < len(nums):
            if nums[current] != 0:
                nums[last_non_zero] = nums[current]
                last_non_zero += 1
            current += 1

        for i in range(last_non_zero, len(nums)):
            nums[i] = 0

@dataclass
class TestCase:
    nums: List[int]
    expectation: List[int]


TESTS = [
    TestCase(
        nums=[0, 1, 0, 3, 12],
        expectation=[1, 3, 12, 0, 0]
    ),
    TestCase(
        nums=[0],
        expectation=[0]
    ),
    TestCase(
        nums=[0, 0, 1],
        expectation=[1, 0, 0]
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                Solution().moveZeroes(t.nums)
                self.assertEqual(t.nums, t.expectation)
