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
        start_color = image[sr][sc]

        if start_color == newColor:
            return image

        MAX_ROW = len(image) - 1
        MAX_COL = len(image[0]) - 1

        stack = [(sr, sc)]

        while stack:
            row, col = stack.pop()
            
            if image[row][col] != start_color:
                continue

            image[row][col] = newColor

            if row + 1 <= MAX_ROW:
                stack.append((row+1, col))
            
            if row - 1 >= 0:
                stack.append((row-1, col))

            if col + 1 <= MAX_COL:        
                stack.append((row, col+1))

            if col - 1 >= 0:
                stack.append((row, col-1))
                
        return image


@ dataclass
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
    ),
    TestCase(
        image=[
            [0, 0, 0],
            [0, 1, 1]
        ],
        sr=1,
        sc=1,
        newColor=1,
        expectation=[
            [0, 0, 0],
            [0, 1, 1]
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
                        sr=t.sr,
                        sc=t.sc,
                        newColor=t.newColor
                    ),
                    t.expectation
                )
