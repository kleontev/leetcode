# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from dataclasses import dataclass
from typing import List, Tuple
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1

        while p2 < len(nums):
            if nums[p2] != nums[p1]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1

        return p1 + 1


@dataclass
class TestCase:
    nums: List[int]
    expected_k: int
    expected_nums: List[int]


TESTS = [
    TestCase([1], 1, [1]),
    TestCase([1, 1], 1, [1, 1]),
    TestCase([1, 2, 2, 3], 3, [1, 2, 3]),
    TestCase([1, 1, 2], 2, [1, 2, None]),
    TestCase([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                k = Solution().removeDuplicates(t.nums)

                self.assertEqual(k, t.expected_k)

                for i in range(k):
                    self.assertEqual(t.nums[i], t.expected_nums[i])
