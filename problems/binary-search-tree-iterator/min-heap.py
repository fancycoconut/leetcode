# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.items = []
        self.i = 0

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            heapq.heappush(self.items, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        #print(self.items)

    def next(self) -> int:
        val = heapq.heappop(self.items)
        return val

    def hasNext(self) -> bool:
        return len(self.items) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()