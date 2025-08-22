class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = inf
        bot = 0
        left = inf
        right = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    top = min(top, i)
                    bot = max(bot, i)
                    left = min(left, j)
                    right = max(right, j)
        
        # print(top)
        # print(bot)
        # print()
        # print(left)
        # print(right)
        return abs((right - left + 1) * (1 + bot - top))