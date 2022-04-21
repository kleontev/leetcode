from dataclasses import dataclass
from typing import List, Optional
import unittest

from util import ListNode, list_to_listnode, listnode_to_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force solution: convert ListNode to array
        # O(n) time O(n) space
        # TODO O(n) time O(1) space 

        all_nodes = []
        node = head

        while node:
            all_nodes.append(node)
            node = node.next

        if n == len(all_nodes):
            # remove first element
            return head.next

        if n == 1:
            # remove last element
            all_nodes[-2].next = None

        else:
            all_nodes[-n-1].next = all_nodes[-n+1]

        return head


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
