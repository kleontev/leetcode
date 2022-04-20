from dataclasses import dataclass
from typing import List, Optional
import unittest

from util import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head

        while True:
            try:
                fast_ptr = fast_ptr.next
                fast_ptr = fast_ptr.next
            except AttributeError:
                return slow_ptr

            slow_ptr = slow_ptr.next


@dataclass
class TestCase:
    head: List[int]
    expectation: List[int]


TESTS = [
    TestCase(
        head=[1, 2, 3, 4, 5],
        expectation=[3, 4, 5]
    ),
    TestCase(
        head=[1, 2, 3, 4, 5, 6],
        expectation=[4, 5, 6]
    ),
    TestCase(
        head=[],
        expectation=[],
    ),
    TestCase(
        head=[0],
        expectation=[0]
    )
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    listnode_to_list(
                        Solution().middleNode(
                            head=list_to_listnode(t.head)
                        )
                    ),
                    t.expectation
                )
