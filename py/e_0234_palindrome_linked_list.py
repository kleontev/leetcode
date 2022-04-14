# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode(val={self.val}, next={self.next})'


def reverse_in_place(head: Optional[ListNode]) -> Optional[ListNode]:
    # reverse linked list in O(n) time and O(1) space
    prev_node = None
    next_node = head

    while next_node:
        this_node = next_node
        next_node = this_node.next

        # reverse
        this_node.next = prev_node
        prev_node = this_node

    return prev_node


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            # empty linked list
            return False

        if head and not head.next:
            # single-element linked list
            return True

        # find the middle of the list using two pointer approach.
        # "fast" pointer advances at 2x speed, so it will reach
        # the end of the list exactly when the "slow" pointer
        # reaches the middle (or the node before the middle
        # if the number of nodes is odd).
        fast_ptr = slow_ptr = head
        while fast_ptr:
            try:
                fast_ptr = fast_ptr.next
                fast_ptr = fast_ptr.next
            except AttributeError:
                break
            slow_ptr = slow_ptr.next

        is_palindrome = True

        # now we perform the actual check.
        # reverse second half of the list in place,
        # then iterate over reversed nodes and compare them
        # with corresponding first half nodes
        # NOTE: this breaks original list (2nd half is unlinked),
        # so we'll have to restore in the end.
        reversed_2nd_half = reverse_in_place(slow_ptr)

        first_half_node = head
        second_half_node = reversed_2nd_half

        while second_half_node:
            if first_half_node.val != second_half_node.val:
                is_palindrome = False
                break

            first_half_node = first_half_node.next
            second_half_node = second_half_node.next

        # restore the original list
        _ = reverse_in_place(reversed_2nd_half)

        return is_palindrome


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()

        tests = [
            (ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4))))), False),
            (ListNode(0, ListNode(1, ListNode(2, ListNode(1, ListNode(0))))), True),
            (ListNode(0, ListNode(1)), False),
            (ListNode(0), True),
            (ListNode(0, ListNode(1, ListNode(0))), True),
            (None, False)
        ]

        for test, expectation in tests:
            with self.subTest(f'testee={test}'):
                self.assertEqual(
                    solution.isPalindrome(test),
                    expectation
                )
