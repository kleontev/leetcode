# https://leetcode.com/problems/implement-strstr/
from dataclasses import dataclass
import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for hp in range(len(haystack) - len(needle) + 1):
            for np in range(len(needle)):
                if haystack[hp + np] != needle[np]:
                    break
            else:
                return hp 
        
        return - 1 


@dataclass
class TestCase:
    haystack: str
    needle: str
    expectation: int


TESTS = [
    TestCase('hello', 'z', -1),
    TestCase('hello', 'h', 0),
    TestCase('hello', 'e', 1),
    TestCase('hello', 'he', 0),
    TestCase('hello', 'lo', 3),
    TestCase('hello', 'o', 4),

]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().strStr(
                        t.haystack,
                        t.needle
                    ),
                    t.expectation
                )
