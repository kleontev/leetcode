# https://leetcode.com/problems/roman-to-integer/
from dataclasses import dataclass
import unittest

values = dict(
    I=1,
    V=5,
    X=10,
    L=50,
    C=100,
    D=500,
    M=1000
)

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev = None
        for c in reversed(s):
            sign = -1 if values[c] < values.get(prev, -1) else 1

            result += sign * values[c]

            prev = c

        return result


@dataclass
class TestCase:
    s: str
    expectation: int


TESTS = [
    TestCase('I', 1),
    TestCase('M', 1000),
    TestCase('III', 3),
    TestCase('LVIII', 58),
    TestCase('MCMXCIV', 1994),
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().romanToInt(t.s),
                    t.expectation
                )
