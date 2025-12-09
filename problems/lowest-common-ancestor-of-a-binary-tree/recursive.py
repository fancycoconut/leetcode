# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        # We found the node matching the value so return the node
        if root.val == p.val or root.val == q.val:
            return root
        
        # Find the nodes on both the left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if we found both sides then the lowest common would be the middle / original root
        if left != None and right != None:
            return root

        # Otherwise return the left one
        if left != None:
            return left

        return right