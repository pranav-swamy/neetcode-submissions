# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        # collect only the last onein each level

        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            children = []
            res.append(queue[-1].val)
            for node in queue:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            queue = children
        
        return res

