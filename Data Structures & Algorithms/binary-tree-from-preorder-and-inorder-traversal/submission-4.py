# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inidx = {v:i for i, v in enumerate(inorder)}
        self.preIdx = 0

        def buildTree(instart, inend):
            if instart > inend:
                return None
            root = TreeNode(preorder[self.preIdx])
            self.preIdx += 1

            in_index = inidx[root.val]
            root.left = buildTree(instart, in_index-1)
            root.right = buildTree(in_index+1, inend)

            return root
        
        return buildTree(0, len(inorder)-1)