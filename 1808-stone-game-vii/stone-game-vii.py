class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones, initial = 0))
        
        @lru_cache(65536)
        # @cache
        def dp(i, j):
            if i == j: 
                return 0
            return max(prefix[j + 1] - prefix[i + 1] - dp(i + 1, j), \
                       prefix[j] - prefix[i] - dp(i, j - 1))
        
        return dp(0, len(stones) - 1)