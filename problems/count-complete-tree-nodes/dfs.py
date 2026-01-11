# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        numOfNodes = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            ans = 1
            ans += dfs(node.left)
            ans += dfs(node.right)

            return ans

        return dfs(root)
