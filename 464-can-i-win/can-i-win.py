class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        candidate = [i+1 for i in range(maxChoosableInteger)]
        if maxChoosableInteger*(maxChoosableInteger+1)//2 < desiredTotal: return False
        memo = {}
        def dp(candidate: List[int], remainingTotal: int) -> bool:
            if candidate[-1] >= remainingTotal:
                return True
            if (candidate, remainingTotal) in memo:
                return memo[candidate, remainingTotal]
            for i in range(len(candidate)):
                if not dp(candidate[:i] + candidate[i + 1:], remainingTotal - candidate[i]):
                    memo[candidate, remainingTotal] = True
                    return True
            memo[candidate, remainingTotal] = False
            return False
        return dp(tuple(candidate), desiredTotal)