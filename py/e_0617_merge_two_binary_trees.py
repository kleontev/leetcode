# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional
from util import TreeNode


class Solution:
    def mergeTrees(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1:
            return root2
        elif not root2:
            return root1

        return TreeNode(
            val=root1.val+root2.val,
            left=self.mergeTrees(root1.left, root2.left),
            right=self.mergeTrees(root1.right, root2.right)
        )
