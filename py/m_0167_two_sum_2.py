from dataclasses import dataclass
from typing import List
import unittest

from util import binary_search


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        while p1 < len(numbers):
            p2 = binary_search(numbers, target - numbers[p1], first=False)

            if p2 == -1:
                p1 += 1
                continue

            return [p1+1, p2+1]


@dataclass
class TestCase:
    numbers: List[int]
    target: int
    expectation: List[int]


TESTS = [
    TestCase(
        numbers=[2, 7, 11, 15],
        target=9,
        expectation=[1, 2],
    ),
    TestCase(
        numbers=[2, 3, 4],
        target=6,
        expectation=[1, 3],
    ),
    TestCase(
        numbers=[-1, 0],
        target=-1,
        expectation=[1, 2],
    ),
    TestCase(
        numbers=[0, 0, 3, 4],
        target=0,
        expectation=[1, 2],
    ),
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().twoSum(t.numbers, t.target),
                    t.expectation
                )
