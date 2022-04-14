# https://leetcode.com/problems/palindrome-number/
import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # there's also an obvious solution to cast num to str
        # and check if str == reversed(str).

        assert x is not None

        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        if x < 10:
            # single-digit number is always a palindrome
            return True

        reversed_x = 0

        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        return x == reversed_x or x == reversed_x // 10


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            (0, True),
            (121, True),
            (-121, False),
            (10, False),
            (123, False)
        ]

        for test, expectation in tests:
            with self.subTest(
                    f'test={test}, '
                    f'expected={expectation}'
            ):
                self.assertEqual(
                    solution.isPalindrome(test),
                    expectation
                )
