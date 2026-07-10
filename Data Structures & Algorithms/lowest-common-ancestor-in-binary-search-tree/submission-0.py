# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if both values of p and q are less than root
        # then lca must be in the left subtree
        # if both values are right, lca must be in the right subtree
        # else, if values are in different subtrees, we found the lca

        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: # both not in left or both not in right
        # both are in different subtrees
            return root # found the lca