# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        output = []

        def preOrderDfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            output.append(node.val)
            preOrderDfs(node.left)
            preOrderDfs(node.right)
        
        preOrderDfs(root)
        #print(output)

        serializedOutput = ",".join(str(val) for val in output)
        #print(serializedOutput)
        return serializedOutput        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        parts = data.split(",")
        if len(parts) == 1 and parts[0] == "":
            return None
        #print(parts)

        def insertBinaryTree(node: Optional[TreeNode], val: int) -> None:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insertBinaryTree(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insertBinaryTree(node.right, val)

        root = TreeNode(int(parts[0]))
        for i in range(1, len(parts)):
            val = int(parts[i])
            insertBinaryTree(root, val)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
