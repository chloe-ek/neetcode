# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prev = float('-inf')
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return True

        if not self.inorder(node.left):
            return False
  
            
        if self.prev >= node.val:
            return False
        else:
            self.prev = node.val

        
        return self.inorder(node.right)
            


        