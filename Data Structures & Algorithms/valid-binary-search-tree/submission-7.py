# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, low, high):
        if not node:
            return True

        if high <= node.val or node.val <= low:
            return False

        left_side = self.helper(node.left, low, node.val)
        right_side = self.helper(node.right, node.val, high)

        return left_side and right_side


        