# https://leetcode.com/problems/climbing-stairs/
from dataclasses import dataclass
import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            # climbed the ladder and found a way
            return 1

        if n == -1:
            # climbed the ladder but wasted a step
            return 0

        # keep climbing
        return self.climbStairs(n-1) + self.climbStairs(n-2)


@dataclass
class TestCase:
    n: int
    expectation: int


TESTS = [
    TestCase(1, 1),
    TestCase(2, 2),
    TestCase(3, 3),
    TestCase(4, 5),
    TestCase(5, 8),
    TestCase(6, 13),
    TestCase(7, 21),
    TestCase(8, 34),
    TestCase(9, 55),
    TestCase(10, 89),
    TestCase(45, 1_836_311_903),
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().climbStairs(t.n),
                    t.expectation
                )
