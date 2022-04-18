from dataclasses import dataclass
from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = p2 = 0
        nums3 = []

        # O(2(m+n)) time, O(m+n) space
        # can we do O(1) space?
        while p1 < m:
            while p2 < n and nums1[p1] > nums2[p2]:
                nums3.append(nums2[p2])
                p2 += 1
            nums3.append(nums1[p1])
            p1 += 1

        while p2 < n:
            nums3.append(nums2[p2])
            p2 += 1

        for i in range(m+n):
            nums1[i] = nums3[i]


@dataclass
class TestCase:
    nums1: List[int]
    m: int
    nums2: List[int]
    n: int
    expectation: List[int]


TESTS = [
    TestCase(
        nums1=[1, 2, 3, 0, 0, 0],
        m=3,
        nums2=[2, 5, 6],
        n=3,
        expectation=[1, 2, 2, 3, 5, 6]
    ),
    TestCase(
        nums1=[4, 5, 6, 0, 0, 0],
        m=3,
        nums2=[1, 2, 3],
        n=3,
        expectation=[1, 2, 3, 4, 5, 6]
    ),
    TestCase(
        nums1=[1],
        m=1,
        nums2=[],
        n=0,
        expectation=[1]
    ),
    TestCase(
        nums1=[0],
        m=0,
        nums2=[1],
        n=1,
        expectation=[1]
    ),

]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        for t in TESTS:
            with self.subTest(t):
                solution.merge(
                    nums1=t.nums1,
                    m=t.m,
                    nums2=t.nums2,
                    n=t.n
                )

                self.assertEqual(
                    t.nums1,
                    t.expectation
                )
