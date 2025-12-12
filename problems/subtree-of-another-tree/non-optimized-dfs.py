# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        visited = set()

        while len(stack) > 0:
            node = stack.pop()
            if node == None:
                continue
            if node in visited:
                continue
            if self.isSame(node, subRoot):
                return True
            
            visited.add(node)
            stack.append(node.left)
            stack.append(node.right)
        return False

    def isSame(self, nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
        if nodeA == None and nodeB == None:
            return True
        if nodeA != None and nodeB == None:
            return False
        if nodeA == None and nodeB != None:
            return False
        if nodeA.val != nodeB.val:
            return False

        leftIsSame = self.isSame(nodeA.left, nodeB.left)
        rightIsSame = self.isSame(nodeA.right, nodeB.right)

        return leftIsSame and rightIsSame
        