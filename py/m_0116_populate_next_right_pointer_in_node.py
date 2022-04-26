# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
from typing import Optional


class Node:
    def __init__(
            self,
            val: int = 0,
            left: 'Node' = None,
            right: 'Node' = None,
            next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return (
            f'Node(val={self.val}, '
            f'left={self.left}, '
            f'right={self.right}, '
            f'next={self.next})'
        )


class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        if not (root and root.left):
            return root

        l, r = root.left, root.right

        # establish pointers from rightmost children of "left"
        # branch to leftmost children of "right" branch
        while l:
            l.next = r
            l = l.right
            r = r.left

        # recurse for both branches
        self.connect(root.left)
        self.connect(root.right)

        return root
