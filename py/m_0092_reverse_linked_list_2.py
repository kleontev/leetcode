# https://leetcode.com/problems/reverse-linked-list-ii/
from dataclasses import dataclass
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode(val={self.val}, next={self.next})'


class Solution:
    def reverseBetween(
            self, head: Optional[ListNode],
            left: int,
            right: int
    ) -> Optional[ListNode]:
        """
        sample input:
        head=[1, 2, 3, 4, 5], left=2, right=4
        expected output: [1, 4, 3, 2, 5]
        step 1: broken state
            [1 -> 2], [2 -> 3],  [3 -> 2], [4 -> 5]
            (unlink 3 from 4 and point it to 2; 1 still points to 2; 2 points to 3 - cycle)
        step 2: broken state
              [1 -> 2], [4 -> 3 -> 2], [2 -> 3], [5]
              (unlink 4 from 5 and point it to 3; 1 still points to 2; 5 is orphaned)
        step 3: valid reversed state
            [1 -> 4 -> 3 -> 2 -> 5]
            (finalize: switch 1's next from 2 to 4, point 2 to 5)
        """

        assert 0 < left <= right

        if not head:
            return None

        if not head.next:
            return head

        if left == right:
            return head

        # nodes 1 and 2 (hereafter referring example above)
        pre_start, start = self.start_pos(
            head=head,
            n=left
        )

        # nodes 4 and 5
        reversed_start, tail = self.reverse_n_nodes(
            head=start,
            n=right - left + 1,
        )

        # finalize: link node 1 to node 4
        if pre_start:
            pre_start.next = reversed_start
        else:
            # left == 1, first node, no pre_start
            head = reversed_start

        # finalize: link node 2 to node 5
        start.next = tail

        return head

    def start_pos(
            self,
            head: ListNode,
            n: int
    ) -> tuple[ListNode, ListNode]:
        assert head

        this_node = None
        next_node = head

        for _ in range(n - 1):  # 1-based to 0-based
            this_node = next_node
            next_node = next_node.next

        # node 1 and 2
        return this_node, next_node

    def reverse_n_nodes(
            self,
            head: ListNode,
            n: int
    ):
        assert head

        prev_node = None
        this_node = None
        next_node = head

        for _ in range(n):
            this_node = next_node
            next_node = this_node.next

            this_node.next = prev_node
            prev_node = this_node

        # node 4 and 5
        return this_node, next_node


@dataclass
class TestCase:
    head: Optional[list[int]]
    left: int
    right: int
    expectation: Optional[list[int]]


def _listnode_from_list(int_list: Optional[list[int]]) -> Optional[ListNode]:
    if not int_list:
        return None
    node = None
    for i in reversed(int_list):
        node = ListNode(i, node)

    return node


def _list_from_listnode(node: ListNode) -> Optional[list[int]]:
    if not node:
        return None
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            TestCase([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
            TestCase([1, 2, 3, 4, 5], 1, 4, [4, 3, 2, 1, 5]),
            TestCase(None, 1, 2, None),
            TestCase([1], 100, 101, [1]),
            TestCase([1, 2], 1, 2, [2, 1]),
        ]

        for t in tests:
            with self.subTest(f'test={t}'):
                self.assertEqual(
                    _list_from_listnode(
                        solution.reverseBetween(
                            _listnode_from_list(t.head),
                            t.left,
                            t.right
                        )
                    ),
                    t.expectation
                )
