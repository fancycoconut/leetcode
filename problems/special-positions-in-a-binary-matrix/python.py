class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        one_positions = []
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    one_positions.append((row, col))

        #print(one_positions)
        ans = 0
        while len(one_positions) > 0:
            pos = one_positions.pop()
            row = pos[0]
            col = pos[1]

            rows_passed = True
            for r in range(rows):
                if r != row and mat[r][col] == 1:
                    rows_passed = False

            cols_passed = True
            for c in range(cols):
                if c != col and mat[row][c] == 1:
                    cols_passed = False

            if rows_passed and cols_passed:
                ans += 1
                    
        return ans
