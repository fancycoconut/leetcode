# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [ (root, 0) ]
        visitedNodes = set()

        levelMap = {}
        numOfLevels = 0
        while len(queue) > 0:
            item = queue.pop(0)
            node = item[0]
            level = item[1]
            if not node or item in visitedNodes:
                continue

            visitedNodes.add(item)
            numOfLevels = max(numOfLevels, level)

            arr = levelMap.get(level, [])
            arr.append(node.val)
            levelMap[level] = arr

            queue.append(( node.left, level + 1 ))
            queue.append(( node.right, level + 1 ))
            
        print(levelMap)
        output = []
        for k,v in levelMap.items():
            output.append(v)

        return output
