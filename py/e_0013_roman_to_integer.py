from dataclasses import dataclass
import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        pass


@dataclass
class TestCase:
    s: str
    expectation: int


TESTS = [
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
