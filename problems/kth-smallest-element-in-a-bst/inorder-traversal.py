# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        
        def inOrderTraversal(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            inOrderTraversal(node.left)
            output.append(node.val)
            inOrderTraversal(node.right)

        inOrderTraversal(root)
        # print(output)

        return output[k-1]
