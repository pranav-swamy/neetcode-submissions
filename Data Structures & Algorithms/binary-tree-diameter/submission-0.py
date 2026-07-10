# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.diam(root)

        return self.diameter
    
    def diam(self, root):
        if not root:
            return 0
        
        left_ht = self.diam(root.left)
        right_ht = self.diam(root.right)

        self.diameter = max(self.diameter, left_ht + right_ht)

        if left_ht > right_ht:
            return 1+ left_ht
        else:
            return 1+ right_ht

                
        