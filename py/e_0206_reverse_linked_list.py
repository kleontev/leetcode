# https://leetcode.com/problems/reverse-linked-list
from typing import Optional, List
import unittest


class ListNode:
    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode(val={self.val}, next={self.next})'


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


def _list_node_to_list(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []

    if not head.next:
        return [head.val]

    node = head
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))),
            ListNode(0, ListNode(1, ListNode(2, ListNode(1, ListNode(0))))),
            ListNode(0, ListNode(1)),
            ListNode(0),
            ListNode(0, ListNode(1, ListNode(0))),
            None
        ]

        for test in tests:
            with self.subTest(f'test={test}'):
                self.assertEqual(
                    list(reversed(_list_node_to_list(test))),
                    _list_node_to_list(solution.reverseList(test))
                )
