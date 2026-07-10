# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []

        def preorder(root):
            if not root:
                ser.append('N')
                return
            ser.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ','.join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        deser = data.split(',')

        def preorder(deser):
            if not deser or deser[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(int(deser[self.i]))
            self.i += 1
            root.left = preorder(deser)
            root.right = preorder(deser)

            return root
        
        return preorder(deser)
            
