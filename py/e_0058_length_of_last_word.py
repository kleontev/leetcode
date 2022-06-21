# https://leetcode.com/problems/length-of-last-word/
from dataclasses import dataclass
import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = len(s)
        length = 0

        while ptr > 0 and (length == 0 or s[ptr] != ' '):
            ptr -= 1
            length += s[ptr] != ' '

        return length


@dataclass
class TestCase:
    s: str
    expectation: int


TESTS = [
    TestCase('Hello    ', 5),
    TestCase('     Hello    ', 5),
    TestCase('Hello world', 5),
    TestCase('   fly me   to   the moon  ', 4),
    TestCase('luffy is still joyboy', 6),
    TestCase('', 0)
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().lengthOfLastWord(t.s),
                    t.expectation
                )
