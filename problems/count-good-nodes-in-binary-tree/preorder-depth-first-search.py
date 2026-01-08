# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Finds the number of good nodes    
        def dfsPreOrder(node: TreeNode, maxValSoFar: int) -> int:
            if not node:
                return 0

            goodNodes = 1 if node.val >= maxValSoFar else 0
            maxValSoFar = max(maxValSoFar, node.val)

            goodNodes += dfsPreOrder(node.left, maxValSoFar)
            goodNodes += dfsPreOrder(node.right, maxValSoFar)

            return goodNodes

        return dfsPreOrder(root, root.val)
