class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        def bfs(row: int, col: int) -> bool:
            if (row, col) in visited:
                return False

            queue = deque()
            queue.append((row, col))

            while len(queue) > 0:
                pos = queue.popleft()
                r, c = pos[0], pos[1]
                if (r, c) in visited:
                    continue

                visited.add((r, c))

                if grid[r][c] == "0": continue
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for direction in directions:
                    rx, cx = r + direction[0], c + direction[1]
                    if rx < 0 or rx >= rows or cx < 0 or cx >= cols:
                        continue

                    queue.append((rx, cx))

            return True
        
        numOfIslands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and bfs(row, col):
                    numOfIslands += 1
        
        return numOfIslands
