# https://leetcode.com/problems/flood-fill/
from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def floodFill(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int
    ) -> List[List[int]]:
        pass


@dataclass
class TestCase:
    image: List[List[int]]
    sr: int
    sc: int
    newColor: int
    expectation:  List[List[int]]


TESTS = [
    TestCase(
        image=[
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ],
        sr=1,
        sc=1,
        newColor=2,
        expectation=[
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().floodFill(
                        image=t.image,
                        sc=t.sr,
                        sc=t.sc,
                        newColor=t.newColor
                    ),
                    t.expectation
                )
