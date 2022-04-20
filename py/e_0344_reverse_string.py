from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        begin = 0
        end = len(s) - 1

        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1


@dataclass
class TestCase:
    s: List[str]
    expectation: List[int]


TESTS = [
    TestCase(
        s=["h", "e", "l", "l", "o"],
        expectation=["o", "l", "l", "e", "h"]
    ),
    TestCase(
        s=["H","a","n","n","a","h"],
        expectation=["h","a","n","n","a","H"]
    ),
    TestCase(
        s=['a', 'b'],
        expectation=['b', 'a']
    )
    
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                Solution().reverseString(t.s)
                self.assertEqual(t.s, t.expectation)
