# https://leetcode.com/problems/add-binary/
from dataclasses import dataclass
import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a

        b = b.rjust(len(a), '0')

        result = ['0'] * len(a)

        carry = False

        for i in range(len(b)):
            ia = len(a) - i - 1
            ib = len(b) - i - 1
            
            if a[ia] == b[ib]:
                result[ia] = '1' if carry else '0'
                carry = a[ia] == '1'
            else:
                result[ia] = '0' if carry else '1'
                

        return ('1' if carry else '') + ''.join(result)


@dataclass
class TestCase:
    a: str
    b: str
    expectation: str


TESTS = [
    TestCase('0', '0', '0'),
    TestCase('0', '1', '1'),
    TestCase('1', '1', '10'),
    TestCase('11', '1', '100'),
    TestCase('1', '11', '100'),
    TestCase('11', '11', '110'),
    TestCase('1010', '1011', '10101'),
    TestCase('1111', '0001', '10000'),
    TestCase('100', '110010', '110110'),
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    Solution().addBinary(t.a, t.b),
                    t.expectation
                )
