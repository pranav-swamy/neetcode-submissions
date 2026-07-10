# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, cur_max):
            
            if not root:
                return None
            
            if root.val >= cur_max:
                self.count += 1
                cur_max = root.val
            
            dfs(root.left, cur_max)
            dfs(root.right, cur_max)
        
        if not root:
            return 0
        
        dfs(root, root.val)

        return self.count
        