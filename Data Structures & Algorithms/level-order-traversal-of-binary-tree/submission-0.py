# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        # start with root node
        # collect vals
        # add children to queue
        # loop
        
        queue = [root]
        while queue:
            children = []
            lvl = []
            for node in queue:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                lvl.append(node.val)
            queue = children
            res.append(lvl)
        
        return res
                


