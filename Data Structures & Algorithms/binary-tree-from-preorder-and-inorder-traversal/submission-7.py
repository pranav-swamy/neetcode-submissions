# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.pre_idx = 0
        self.in_idx1 = {v:i for i, v in enumerate(inorder)}

        def buildtree(in_start, in_end):
            if in_start > in_end:
                return None

            in_idx = self.in_idx1[preorder[self.pre_idx]]

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            root.left = buildtree(in_start, in_idx-1)
            root.right = buildtree(in_idx+1, in_end)

            return root
        
        return buildtree(0, len(inorder)-1)


        