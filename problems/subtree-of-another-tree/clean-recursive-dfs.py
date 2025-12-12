# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True

        isLeftSubtree = self.isSubtree(root.left, subRoot)
        isRightSubtree = self.isSubtree(root.right, subRoot)

        return isLeftSubtree or isRightSubtree

    def isSame(self, nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
        if nodeA == None and nodeB == None:
            return True
        if nodeA and nodeB and nodeA.val == nodeB.val:
            leftIsSame = self.isSame(nodeA.left, nodeB.left)
            rightIsSame = self.isSame(nodeA.right, nodeB.right)
            return leftIsSame and rightIsSame

        return False
        