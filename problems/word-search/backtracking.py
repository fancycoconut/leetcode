class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(row: int, col: int, wordIndex: int) -> bool:
            if wordIndex == len(word):
                return True

            if (row, col) in visited \
                or row < 0 or col < 0 or row >= rows or col >= cols \
                or wordIndex >= len(word) \
                or board[row][col] != word[wordIndex]:
                return False
            
            visited.add((row, col))

            a = backtrack(row - 1, col, wordIndex + 1)
            b = backtrack(row + 1, col, wordIndex + 1)
            c = backtrack(row, col - 1, wordIndex + 1)
            d = backtrack(row, col + 1, wordIndex + 1)

            visited.remove((row, col))

            return a or b or c or d

        i = 0
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, i):
                    return True

        return False
