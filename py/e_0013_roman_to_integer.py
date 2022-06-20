# https://leetcode.com/problems/roman-to-integer/
from dataclasses import dataclass
import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        assert len(s) > 0

        NUMBERS = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )

        # if len(s) == 1:
            # return NUMBERS[s[0]]

        result = 0

        prev = None

        for c in reversed(s):
            if NUMBERS[c] < NUMBERS.get(prev, -1):
                result -= NUMBERS[c]
            else:
                result += NUMBERS[c]
            prev = c
        return result


# LVIII
# 1) result += 1
# 2) result += 1


@dataclass
class TestCase:
    s: str
    expectation: int


TESTS = [
    TestCase('I', 1),
    TestCase('M', 1000),
    TestCase('III', 3),
    TestCase('LVIII', 58),
    TestCase('MCMXCIV', 1994), # MCMXCIV 5-1+50-10+1000
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().romanToInt(t.s),
                    t.expectation
                )
