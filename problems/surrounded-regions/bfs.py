class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        visited = set()
        def bfs(row: int, col: int) -> None:
            if (row, col) in visited:
                return

            queue = deque()
            queue.append((row, col))

            while len(queue) > 0:
                pos = queue.popleft()
                r, c = pos[0], pos[1]
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                board[r][c] = "T"

                directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
                for direction in directions:
                    rx, cx = r + direction[0], c + direction[1]

                    if rx < 0 or rx >= rows or cx < 0 or cx >= cols:
                        continue
                    
                    if board[rx][cx] == "O":
                        queue.append((rx, cx))

        # def printBoard(board: List[List[str]]) -> None:
        #     for row in range(rows):
        #         output = []
        #         for col in range(cols):
        #             output.append(board[row][col])

        #         print("".join(output))

        # Mark all Os around the edge as T
        for col in range(cols):
            # Top
            if board[0][col] == "O":
                bfs(0, col)
            # Bottom
            if board[rows - 1][col] == "O":
                bfs(rows - 1, col)

        for row in range(rows):
            # Left
            if board[row][0] == "O":
                bfs(row, 0)
            # Right
            if board[row][cols - 1] == "O":
                bfs(row, cols - 1)

        # Mark all Os as Xs
        # Restore O's from Ts
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

                if board[row][col] == "T":
                    board[row][col] = "O"
        
                    