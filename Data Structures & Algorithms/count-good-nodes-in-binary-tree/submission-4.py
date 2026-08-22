# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, max_val: float = float('-inf')) -> int:
        if not root:
            return 0

        good_counter = 0
        
        if root.val >= max_val:
            good_counter += 1
            max_val = root.val

        good_counter += self.goodNodes(root.left, max_val)
        good_counter += self.goodNodes(root.right, max_val)

        return good_counter
        