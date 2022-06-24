# https://leetcode.com/problems/sqrtx/
import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        prev_guess = x
        guess = 0.5 * (prev_guess + x / prev_guess)

        while abs(guess - prev_guess) >= 1:
            prev_guess = guess
            guess = 0.5 * (prev_guess + x / prev_guess)

        return int(guess)


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in range(1_000_000):
            self.assertEqual(
                Solution().mySqrt(t),
                int(t ** 0.5)
            )
