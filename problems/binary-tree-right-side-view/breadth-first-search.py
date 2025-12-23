# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        if not root:
            return levels

        def traverse(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            
            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)

            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse(root, 0)
        output = []
        for level in levels:
            output.append(level[-1])

        return output
        