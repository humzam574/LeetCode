class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #robot one goes down at the point where the bottom prefix is greater than the top prefix
        #blue will only go down at start if red always stays up, otherwise it stays up the whole time
        #process grid and then go through to find the cutoff point and set it to zero
        
        #at each point calculate what the score will be for robot 2 if it starts bottom or stays up top
        #keep two variables and an ans var

        # top = sum(grid[0][1:])
        # bot = 0
        # ans = top
        # for i in range(1, len(grid[0])):
        #     top -= grid[0][i]
        #     bot += grid[1][i - 1]
        #     ans = min(ans, max(top, bot))
        #     if bot == ans: break #== or >= ?
        # return ans

        bot, i, flag = 0, 1, True; top = ans = sum(grid[0][1:])
        while i < len(grid[0]) and flag: top, bot, i = top - grid[0][i], bot + grid[1][i - 1], i + 1; ans = min(ans, max(top, bot)); flag = bot != ans #!= or < ?
        return ans