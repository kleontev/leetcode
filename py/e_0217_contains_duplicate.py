from typing import List
import unittest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered = set()

        for n in nums:
            if n in encountered:
                return True
            encountered.add(n)

        return False


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([], False),
            ([1], False)
        ]

        for test, expectation in tests:
            with self.subTest(
                f'test={test}'
                f'expectation={expectation}'
            ):
                self.assertEqual(
                    solution.containsDuplicate(test),
                    expectation
                )
