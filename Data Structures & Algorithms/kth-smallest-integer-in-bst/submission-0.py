# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.inorder(root, k)

    def inorder(self, root, k):
        if not root:
            return 0
        ans = 0
        ans = self.inorder(root.left, k)
        if ans > 0:
            return ans
        self.count += 1
        if self.count == k:
            return root.val
        ans = self.inorder(root.right, k)
        if ans > 0:
            return ans
        return 0