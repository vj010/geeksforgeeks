class Solution:
    def antiDiagonalPattern(self, matrix):
        # Code here
        m = len(matrix)
        n = m
        diagonal = []
        for i in range(m):
            col = 0 if i == 0 else n - 1
            for j in range(col, n):
                # print(f"mat:{matrix[i][j]}")
                current_row = i
                current_col = j
                while current_row < n and current_col >= 0:
                    diagonal.append(matrix[current_row][current_col])
                    current_row += 1
                    current_col -= 1
        return diagonal


sol = Solution()
print(sol.antiDiagonalPattern([[1, 2], [3, 4]]))
print(sol.antiDiagonalPattern([[3, 2, 3], [4, 5, 1], [7, 8, 9]]))
print(sol.antiDiagonalPattern([[1]]))
print(
    sol.antiDiagonalPattern(
        [[3, 2, 3, 4], [4, 5, 1, 4], [7, 8, 9, 4], [10, 11, 12, 13]]
    )
)
