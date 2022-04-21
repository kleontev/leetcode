from dataclasses import dataclass
from typing import List, Optional
import unittest

from util import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer, O(n) time O(1) space
        dummy = ListNode(None, head)
        
        fast_ptr = slow_ptr = dummy 

        for _ in range(n + 1):
            fast_ptr = fast_ptr.next

        while fast_ptr: 
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next

        slow_ptr.next = slow_ptr.next.next

        return dummy.next

        



@dataclass
class TestCase:
    head: List[int]
    n: int
    expectation: List[int]


TESTS = [
    TestCase(
        head=[1, 2, 3, 4, 5],
        n=2,
        expectation=[1, 2, 3, 5]
    ),
    TestCase(
        head=[1],
        n=1,
        expectation=[]
    ),
    TestCase(
        head=[1, 2],
        n=1,
        expectation=[1]
    ),
]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    listnode_to_list(
                        Solution().removeNthFromEnd(
                            head=list_to_listnode(t.head),
                            n=t.n
                        )
                    ),
                    t.expectation
                )
