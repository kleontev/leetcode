# https://leetcode.com/problems/reverse-linked-list
from typing import Optional
import unittest

from util import ListNode, listnode_to_list, list_to_listnode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        prev_node = None
        next_node = head

        while next_node:
            this_node = next_node
            next_node = this_node.next

            # reverse
            this_node.next = prev_node
            prev_node = this_node

        return prev_node


class TestSolution(unittest.TestCase):
    def test_solution(self):
        tests = [
            [0, 1, 2, 3, 4],
            [0, 1, 2, 1, 0],
            [0, 1],
            [0],
            [0, 1, 0],
            None
        ]

        for test in tests:
            with self.subTest(f'test={test}'):
                self.assertEqual(
                    listnode_to_list(
                        Solution().reverseList(
                            list_to_listnode(test)
                        )
                    ),
                    list(reversed(test or [])),
                )
