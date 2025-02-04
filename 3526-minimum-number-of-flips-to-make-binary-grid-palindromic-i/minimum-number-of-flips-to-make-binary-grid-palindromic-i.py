class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        a1 = 0
        for x in range(len(grid)):
            l = 0
            r = n - 1
            curr = 0
            while l < r:
                if grid[x][l] != grid[x][r]:
                    curr += 1
                l += 1
                r -= 1
            curr = min(curr, n - curr)
            a1 += curr
        a2 = 0
        for y in range(n):
            curr = 0
            l = 0
            r = m - 1
            while l < r:
                if grid[l][y] != grid[r][y]:
                    curr += 1
                l += 1
                r -= 1
            curr = min(curr, m - curr)
            a2 += curr
        return min(a1, a2)