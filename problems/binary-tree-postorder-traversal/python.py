# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        self.traverse(root, output)

        return output
        
    def traverse(self, node: Optional[TreeNode], output: List[int]):
        if node == None:
            return
        
        self.traverse(node.left, output)
        self.traverse(node.right, output)
        output.append(node.val)
        