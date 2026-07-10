# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbal = True

        self.isBalanc(root)

        return self.isbal

    def isBalanc(self, root):
        if not root:
            return 0
        left_ht = self.isBalanc(root.left)
        right_ht = self.isBalanc(root.right)

        if abs(left_ht - right_ht) > 1:
            self.isbal = False

        return 1 + max(left_ht, right_ht)
