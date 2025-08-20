class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #tabulate from i and j
        #the value is how many new squares you can make with that 1

        #[0, 1, 1, 1]
        #[1, 1, 2, 2]
        #[0, 1, 2, 3]

        m = len(matrix)
        n = len(matrix[0])

        ans = [[0] * n for i in range(m)]

        #2 -> 1
        #3 -> 2
        #4 -> 3
        #go up and to the right and count

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    ans[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    ans[i][j] = min(ans[i-1][j-1], ans[i][j-1], ans[i-1][j]) + 1
        # for row in ans:
        #     print(row)
        return sum(sum(a) for a in ans)


        #[1, 0, 1]
        #[1, 1, 0]
        #[1, 2, 0]