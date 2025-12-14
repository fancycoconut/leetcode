# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfsValid(node, leftBound, rightBound):
            if node == None:
                return True
            if not (node.val < rightBound and node.val > leftBound):
                return False

            return (dfsValid(node.left, leftBound, node.val) and
                dfsValid(node.right, node.val, rightBound))

        return dfsValid(root, float("-inf"), float("inf"))
