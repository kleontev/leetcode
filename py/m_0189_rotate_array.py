from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        O(n) time, O(k) space
        TODO: O(1) space? what would time complexity be?
        """

        # we don't need multiple rotations
        k = k % len(nums)

        if k == 0:
            return

        nums_k = nums[-k:]

        for i in range(len(nums)-k, 0, -1):
            nums[i-1+k] = nums[i-1]

        for i in range(len(nums_k)):
            nums[i] = nums_k[i]


@dataclass
class TestCase:
    nums: List[int]
    k: int
    expectation: List[int]


TESTS = [
    TestCase(
        nums=[1, 2, 3, 4, 5, 6, 7],
        k=3,
        expectation=[5, 6, 7, 1, 2, 3, 4]
    ),
    TestCase(
        nums=[1, 2, 3, 4, 5, 6, 7],
        k=24,
        expectation=[5, 6, 7, 1, 2, 3, 4]
    ),
    TestCase(
        nums=[-1, -100, 3, 99],
        k=2,
        expectation=[3, 99, -1, -100]
    ),
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                Solution().rotate(nums=t.nums, k=t.k)
                self.assertEqual(t.nums, t.expectation)
