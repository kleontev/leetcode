from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pass


@dataclass
class TestCase:
    mat: List[List[int]]
    expectation: List[List[int]]


TESTS = [
    TestCase(
        mat=[
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        expectation=[
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ),
    TestCase(
        mat=[
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ],
        expectation=[
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1]
        ]
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().updateMatrix(mat=t.mat),
                    t.expectation
                )
