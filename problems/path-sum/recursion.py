# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        print(root.val)
        remainingSum = targetSum - root.val

        if root.left is None and root.right is None:
            return remainingSum == 0

        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)