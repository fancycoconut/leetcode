class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
        def bfs(r: int, c: int, visited: set) -> None:
            if (r, c) in visited: return

            queue = deque()
            queue.append((r, c))

            while len(queue) > 0:
                pos = queue.popleft()
                row, col = pos[0], pos[1]
                if (row, col) in visited:
                    continue

                height = heights[row][col]
                visited.add((row, col))

                for direction in directions:
                    rx, cx = row + direction[0], col + direction[1]
                    if rx < 0 or rx >= rows or cx < 0 or cx >= cols:
                        continue
                    if heights[rx][cx] >= height:
                        queue.append((rx, cx))

        pacificLocations = set()
        atlanticLocations = set()
        for col in range(cols):
            bfs(0, col, pacificLocations) # Top row
            bfs(rows - 1, col, atlanticLocations)
        
        for row in range(rows):
            bfs(row, 0, pacificLocations) # Left col
            bfs(row, cols - 1, atlanticLocations) # Right col

        ans = []
        # Union locations
        for pos in pacificLocations:
            if pos in atlanticLocations:
                ans.append([ pos[0], pos[1]  ])
        
        return ans
