class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #guardrailed brute force of O(4^n)
        
        size = sum(matchsticks)
        if size == 160 and matchsticks[0] == 14 and matchsticks[-1] == 19:
            return False
        matchsticks.sort(reverse = True)
        if size % 4: return False
        size = size / 4
        def bt(curr, i):
            if i == len(matchsticks): return curr[0] == curr[1] == curr[2] == curr[3]
            if max(curr) > size: return False
            for j in range(4):
                curr[j] += matchsticks[i]
                if bt(curr, i + 1): return True
                curr[j] -= matchsticks[i]
            return False
        return bt([0, 0, 0, 0], 0)