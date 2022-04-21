from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(1) space, O(n^2) time 
        ptr_string = 0
        current_longest = 0

        while ptr_string < len(s):
            chars = set()
            ptr_substring = ptr_string

            while ptr_substring < len(s) and s[ptr_substring] not in chars:
                chars.add(s[ptr_substring])
                ptr_substring += 1

            current_longest = max(current_longest, len(chars))

            ptr_string += 1

        return current_longest


@dataclass
class TestCase:
    s: str
    expectation: int


TESTS = [
    TestCase(
        s="abcabcbb",
        expectation=3
    ),
    TestCase(
        s='b' * 5,
        expectation=1
    ),
    TestCase(
        s='pwwkew',
        expectation=3
    ),
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().lengthOfLongestSubstring(t.s),
                    t.expectation
                )
