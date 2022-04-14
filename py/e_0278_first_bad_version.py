from typing import List
import unittest

BAD_VERSION = None

# The isBadVersion API is already defined for you.


def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        version = -1

        while left <= right:
            version = (left + right) // 2

            if isBadVersion(version):
                if not isBadVersion(version - 1):
                    break

                right = version - 1

            else:
                left = version + 1

        return version


class TestSolution(unittest.TestCase):
    def test_first_bad(self):
        solution = Solution()

        tests = [
            (5, 4),
            (1, 1),
            (3, 2)
        ]

        global BAD_VERSION

        for total, first_bad in tests:
            with self.subTest(f"total={total}, first_bad={first_bad}"):
                BAD_VERSION = first_bad
                self.assertEqual(
                    solution.firstBadVersion(total),
                    first_bad
                )
