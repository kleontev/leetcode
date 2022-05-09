# https://leetcode.com/problems/permutation-in-string/submissions/
from dataclasses import dataclass
from typing import List
import unittest


def get_char_count(string: str) -> dict:
    count = {}
    for char in string:
        try:
            count[char] += 1
        except KeyError:
            count[char] = 1

    return count


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # idea: a sliding window of s2 sized len(s1)
        # should contain the same letter counts as s1.
        # O(1) space, O(s2^2) time - slow. can we do faster?
        # TODO do not invoke get_char_count on every iteration, 
        # maintain a rolling window count instead
        s1_counts = get_char_count(s1)

        for i in range(len(s2)-len(s1)+1):
            if get_char_count(s2[i:i+len(s1)]) == s1_counts:
                return True

        return False


@dataclass
class TestCase:
    s1: str
    s2: str
    expectation: bool


TESTS = [
    TestCase(
        s1='ab',
        s2='eidbaooo',
        expectation=True
    ),
    TestCase(
        s1='ab',
        s2='eidboaoo',
        expectation=False
    ),
    TestCase(
        s1='adc',
        s2='dcda',
        expectation=True
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().checkInclusion(t.s1, t.s2),
                    t.expectation
                )
