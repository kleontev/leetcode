from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        # technically it's O(n) space
        s += ' '
        
        ptr_last_space = -1
        new_string = []

        for ptr_sentence in range(len(s)):
            if s[ptr_sentence] != ' ':
                continue

            for ptr_word in range(ptr_sentence-1, ptr_last_space, -1):
                new_string.append(s[ptr_word])
            new_string.append(' ')

            ptr_last_space = ptr_sentence

        return ''.join(new_string)[:-1]


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
