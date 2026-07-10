# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = -1
        self.inorder(root, k)
        return self.res

    def inorder(self, root, k):
        if not root:
            return 0
        
        self.inorder(root.left, k)
        
        self.count += 1
        if self.count == k:
            self.res = root.val
        self.inorder(root.right, k)
        