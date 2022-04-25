# https://leetcode.com/problems/max-area-of-island/
from dataclasses import dataclass
from typing import List
import unittest


def get_area(
    grid: List[List[int]],
    seen: set,
    row: int,
    col: int
) -> int:
    if not (
            0 <= row < len(grid)
        and 0 <= col < len(grid[0])
        and grid[row][col] == 1
        and (row, col) not in seen
    ):
        return 0

    seen.add((row, col))

    return (
        1 
        + get_area(grid, seen, row + 1, col)
        + get_area(grid, seen, row - 1, col)
        + get_area(grid, seen, row, col + 1)
        + get_area(grid, seen, row, col - 1)
    )


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        return max(
            get_area(grid, seen, r, c)
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )


@ dataclass
class TestCase:
    grid: List[List[int]]
    expectation:  int


TESTS = [
    TestCase(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ],
        expectation=6,
    ),
    TestCase(
        grid=[
            [0, 1, 1, 0],
            [0, 1, 0, 1]
        ],
        expectation=3
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().maxAreaOfIsland(
                        grid=t.grid
                    ),
                    t.expectation
                )
