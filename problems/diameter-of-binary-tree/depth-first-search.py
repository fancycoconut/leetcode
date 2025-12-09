# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root: Optional[TreeNode]):
            nonlocal diameter
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            diameter = max(diameter, left + right)

            # Max because we only want the longest path from either left or right
            return 1 + max(left, right)

        dfs(root)
        return diameter