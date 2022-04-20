from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))


@dataclass
class TestCase:
    s: List[str]
    expectation: List[int]


TESTS = [
    TestCase(
        s="Let's take LeetCode contest",
        expectation="s'teL ekat edoCteeL tsetnoc"
    ),
    TestCase(
        s="God Ding",
        expectation="doG gniD"
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().reverseWords(t.s),
                    t.expectation
                )
