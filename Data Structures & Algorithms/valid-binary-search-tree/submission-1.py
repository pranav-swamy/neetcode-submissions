# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBst(root, -float('inf'), float('inf'))
    
    def isValidBst(self, root, leftval, rightval):
        if not root:
            return True
        
        cur_tree = root.val < rightval and root.val > leftval
        left_tree = self.isValidBst(root.left, leftval, root.val)
        right_tree = self.isValidBst(root.right, root.val, rightval)

        return cur_tree and left_tree and right_tree