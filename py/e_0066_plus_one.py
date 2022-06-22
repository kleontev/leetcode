# https://leetcode.com/problems/plus-one/
from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = [0] + digits

        for p in reversed(range(len(new_digits))):
            if new_digits[p] < 9:
                new_digits[p] += 1
                break
            new_digits[p] = 0

        return new_digits if new_digits[0] > 0 else new_digits[1:]


@dataclass
class TestCase:
    digits: List[int]
    expectation: List[int]


TESTS = [
    TestCase([0], [1]),
    TestCase([9, 9, 9], [1, 0, 0, 0]),
    TestCase([1, 2, 3], [1, 2, 4]),
    TestCase([4, 3, 9, 9], [4, 4, 0, 0]),
    TestCase([4, 3, 9, 9], [4, 4, 0, 0]),
    TestCase([4, 3, 2, 1], [4, 3, 2, 2]),
    TestCase([9], [1, 0])
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().plusOne(t.digits),
                    t.expectation
                )
