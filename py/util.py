from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}(val={self.val}, next={self.next})'


def list_to_listnode(int_list: Optional[List[int]]) -> Optional[ListNode]:
    if not int_list:
        return None

    node = None

    for i in reversed(int_list):
        node = ListNode(i, node)

    return node


def listnode_to_list(list_node: Optional[ListNode]) -> Optional[List[int]]:
    if not list_node:
        return []

    if not list_node.next:
        return [list_node.val]

    node = list_node
    result = []

    while node:
        result.append(node.val)
        node = node.next

    return result


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right


def treenode_to_list(
    tree_node: Optional[TreeNode]
) -> Optional[List[int]]:
    raise NotImplementedError


def list_to_treenode(
        int_list: Optional[List[int]]
) -> Optional[TreeNode]:
    raise NotImplementedError


def binary_search(nums: List[int], target: int, first: bool = True) -> int:
    result = -1

    if not nums:
        return result

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            if first:
                right = mid - 1
            else:
                left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return result
