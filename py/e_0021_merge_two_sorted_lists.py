# https://leetcode.com/problems/merge-two-sorted-lists/
from dataclasses import dataclass
from typing import Optional
import unittest

from py.util import ListNode, listnode_to_list, list_to_listnode


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1 = list1
        node2 = list2

        node = ListNode()
        head = node

        while node1 or node2:
            if not node1:
                node.next = ListNode(node2.val)
                node2 = node2.next
            elif not node2:
                node.next = ListNode(node1.val)
                node1 = node1.next
            elif node1.val < node2.val:
                node.next = ListNode(node1.val)
                node1 = node1.next
            else:
                node.next = ListNode(node2.val)
                node2 = node2.next

            node = node.next

        return head.next






@dataclass
class TestCase:
    list1: Optional[ListNode]
    list2: Optional[ListNode]
    expectation: Optional[ListNode]

TESTS = [
    TestCase(list1=[], list2=[], expectation=[]),
    TestCase(list1=[], list2=[0], expectation=[0]),
    TestCase(list1=[1,2,4], list2=[1,3,4], expectation=[1,1,2,3,4,4]),
]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        for t in TESTS:
            with self.subTest(t):
                self.assertEqual(
                    listnode_to_list(
                        Solution().mergeTwoLists(
                            list_to_listnode(t.list1),
                            list_to_listnode(t.list2)
                        )
                    ),
                    t.expectation
                )
